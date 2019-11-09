from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import (CreateAPIView, ListAPIView,
    RetrieveAPIView, UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .filters import *
from .models import *
from .serializers import *


class ServiceViewset(viewsets.ModelViewSet):
    model = Service
    queryset = Service.objects.all().order_by('-id').prefetch_related(
        'ratings'
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
    queryset = Rent.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = RentFilter
