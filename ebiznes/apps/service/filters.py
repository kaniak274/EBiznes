from django_filters import rest_framework as filters

from .models import *


class ServiceFilter(filters.FilterSet):
    professions = filters.CharFilter(field_name='profession__name', lookup_expr='icontains')

    class Meta:
        model = Service
        fields = ['owner', 'professions', 'city']

