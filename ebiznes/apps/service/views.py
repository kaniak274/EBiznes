from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .filters import *
from .models import *
from .serializers import ProfessionSerializer, ServiceSerializer


class ServiceViewset(viewsets.ModelViewSet):
    model = Service
    serializer_class = ServiceSerializer
    queryset = Service.objects.all().order_by('-id').prefetch_related(
        'ratings'
    ).select_related('profession')
    filter_backends = [DjangoFilterBackend]
    filterset_class = ServiceFilter

    def get_permissions(self):
        actions = ['create', 'update', 'partial_update']

        if self.action in actions:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProfessionListView(ListAPIView):
    queryset = Profession.objects.all().order_by('id')
    serializer_class = ProfessionSerializer
    permission_classes = []
    pagination_class = None

