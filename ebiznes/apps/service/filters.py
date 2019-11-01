from django_filters import rest_framework as filters

from .models import *


class ServiceFilter(filters.FilterSet):
    profession = filters.CharFilter(field_name='profession__name', lookup_expr='icontains')
    city = filters.CharFilter(field_name='city', lookup_expr='icontains')

    class Meta:
        model = Service
        fields = ['owner', 'profession', 'city']

