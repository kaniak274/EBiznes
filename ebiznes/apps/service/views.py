from django.http import Http404
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action
from rest_framework.generics import (CreateAPIView, DestroyAPIView, ListAPIView,
    RetrieveAPIView, UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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

        data = request.data
        data.update({
            'service': pk,
            'user': request.user.pk,
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
