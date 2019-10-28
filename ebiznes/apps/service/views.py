from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import ServiceSerializer


class ServiceViewset(viewsets.ModelViewSet):
    model = Service
    serializer_class = ServiceSerializer
    queryset = Service.objects.all().order_by('id').prefetch_related(
        'ratings'
    ).select_related('profession')

    def get_permissions(self):
        actions = ['create', 'update', 'partial_update']

        if self.action in actions:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

