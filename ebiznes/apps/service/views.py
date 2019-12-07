from decimal import Decimal
import json
import requests
from urllib import parse

from django.conf import settings
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action
from rest_framework.generics import (CreateAPIView, DestroyAPIView, ListAPIView,
    RetrieveAPIView, UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .choices import PENDING
from .filters import *
from .models import *
from .serializers import *


class ServiceViewset(viewsets.ModelViewSet):
    model = Service
    queryset = Service.objects.all().order_by('-id').prefetch_related(
        'ratings', 'price_list'
    ).select_related('profession')
    filter_backends = [DjangoFilterBackend]
    filterset_class = ServiceFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DetailServiceSerializer
        else:
            return ServiceSerializer

    def get_permissions(self):
        actions = ['create', 'update', 'partial_update', 'rent_service']

        if self.action in actions:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['post'])
    def rent_service(self, request, pk=None):
        service = self.get_object()

        price_list = request.data.pop('price_list', [])

        if not price_list:
            return Response(
                {'price_list': ['Musisz wybrać co najmniej jeden rekord']},
                status=status.HTTP_400_BAD_REQUEST
            )

        total_price = PriceList.calculate_total_price(price_list)['price__sum']

        data = request.data
        data.update({
            'service': pk,
            'user_id': request.user.pk,
            'total_price': Decimal(total_price),
        })

        serializer = RentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfessionListView(ListAPIView):
    queryset = Profession.objects.all().order_by('id')
    serializer_class = ProfessionSerializer
    permission_classes = []
    pagination_class = None


class CreateRatingAPIView(CreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UpdateRating(UpdateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]
    queryset = Rating.objects.all()

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)


class CheckRatingAPIView(RetrieveAPIView):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]
    queryset = Service.objects.all()

    def get_object(self):
        service = super().get_object()

        rating = service.ratings.filter(owner=self.request.user.pk).first()

        if not rating:
            raise Http404

        return rating


class RentListAPIView(ListAPIView):
    serializer_class = RentSerializer
    queryset = Rent.objects.all().order_by('-modified')
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = RentFilter


class CreatePriceListRecord(CreateAPIView):
    serializer_class = PriceListSerializer
    permission_classes = [IsAuthenticated]

    def check_permissions(self, request):
        super().check_permissions(request)

        service = request.data.get('service', None)

        if service:
            service = get_object_or_404(Service, id=service)

            if not service.owner == request.user:
                raise PermissionDenied()

class RemovePriceListRecord(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PriceList.objects.all()

    def check_object_permissions(self, request, obj):
        super().check_object_permissions(request, obj)

        if not obj.service.owner == request.user:
            raise PermissionDenied()


class UpdatePriceListRecord(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PriceListSerializer
    queryset = PriceList.objects.all()

    def check_object_permissions(self, request, obj):
        super().check_object_permissions(request, obj)

        if not obj.service.owner == request.user:
            raise PermissionDenied()


class UpdateRentView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RentSerializer
    queryset = Rent.objects.all()

    def check_objectt_permissions(self, request, obj):
        super().check_object_permissions(request, obj)

        if not obj.service.owner == request.user:
            raise PermissionDenied()


class RentRetrieveView(RetrieveAPIView):
    permission_classes = []
    serializer_class = RentSerializer
    queryset = Rent.objects.all()


def payment_view(request, pk):
    rent = get_object_or_404(Rent, pk=pk)

    return render(request, 'base.html')


class CreatePaymentAPIView(APIView):
    permission_classes = []

    def post(self, request, pk):
        rent = get_object_or_404(Rent.objects.select_related('service', 'user'), pk=pk)

        access_token = self._get_oauth_token()

        if not access_token:
            return Response(
                'OAuth token nie może zostać pobrany. Skontaktuj się z administratorem.',
                status=status.HTTP_400_BAD_REQUEST
            )

        order_data = self._get_order_data(request, rent)
        headers = {
            'Authorization': 'Bearer {}'.format(access_token),
            'Content-Type': 'application/json; UTF-8',
        }

        response = requests.post(settings.PAYU_ORDER_URL, order_data, headers=headers)

        if response.status_code == status.HTTP_200_OK:
            order_id = parse.parse_qs(parse.urlparse(response.url).query)['orderId'][0]

            Order.objects.create(
                status=PENDING,
                totalAmount='{}'.format((rent.total_price + 1) * 100).split('.')[0],
                order_id=order_id,
                user=rent.user
            )

            return Response({'redirectURI': response.url})

        return Response(
            'Proszę spróbować ponownie za kilka minut',
            status=status.HTTP_400_BAD_REQUEST
        )

    def _get_oauth_token(self):
        data = {
            'grant_type': 'client_credentials',
            'client_id': settings.PAYU_CLIENT_ID,
            'client_secret': settings.PAYU_CLIENT_SECRET,
        }

        response = requests.post(settings.PAYU_OAUTH_URL, data)

        if response.status_code == status.HTTP_200_OK:
            return response.json()['access_token']
        else:
            return None

    def _get_order_data(self, request, rent):
        order_data = {
            'customerIp': request.META.get('REMOTE_ADDR'),
            'merchantPosId': settings.PAYU_POS_ID,
            'description': 'Zapłata za usługę {}'.format(rent.service.name),
            'currencyCode': 'PLN',
            'totalAmount': '{}'.format((rent.total_price + 1) * 100).split('.')[0],
            'products': [
                {
                    'name': 'Usługa {}'.format(rent.service.name),
                    'unitPrice': '{}'.format((rent.total_price + 1) * 100).split('.')[0],
                    'quantity': '1'
                }
            ]
        }

        return json.dumps(order_data)