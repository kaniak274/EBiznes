from django.contrib.auth import get_user_model

from rest_auth.serializers import UserDetailsSerializer

from rest_framework import serializers

from .models import *


class PriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = ('pk', 'name', 'price', 'service')
        extra_kwargs = {
            'service': {'write_only': True}
        }


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ('pk', 'name')


class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.DecimalField(max_digits=3, decimal_places=2,
        min_value=0, max_value=5, write_only=True)
    owner_data = UserDetailsSerializer(read_only=True, source='owner')
    rating_value = serializers.FloatField(read_only=True, source='rating')

    class Meta:
        model = Rating
        fields = ('pk', 'owner', 'rating', 'comment', 'service', 'owner_data', 'modified',
            'rating_value')
        extra_kwargs = {
            'owner': {'required': False, 'write_only': True},
            'service': {'write_only': True},
            'modified': {'read_only': True},
        }


class ServiceSerializer(serializers.ModelSerializer):
    profession = ProfessionSerializer(read_only=True)
    profession_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Profession.objects.all(), source='profession')

    class Meta:
        model = Service
        fields = ('pk', 'name', 'description', 'owner', 'profession',
            'profession_id', 'city', 'street', 'service_logo', 'phone_number',
            'created', 'rate')
        extra_kwargs = {
            'owner': {'required': False},
        }


class DetailServiceSerializer(ServiceSerializer):
    random_ratings = RatingSerializer(many=True, read_only=True)
    price_list = PriceListSerializer(read_only=True, many=True)

    class Meta(ServiceSerializer.Meta):
        fields = ('pk', 'name', 'description', 'owner', 'profession',
            'profession_id', 'city', 'street', 'service_logo', 'phone_number',
            'created', 'rate', 'random_ratings', 'price_list')


class RentSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(max_length=255, read_only=True, source='service.name')
    status_display = serializers.SerializerMethodField()
    user = UserDetailsSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=get_user_model().objects.all(), source='user')

    class Meta:
        model = Rent
        fields = ('pk', 'created', 'service', 'user', 'modified',
            'status', 'phone_number', 'address', 'service_name', 'status_display',
            'total_price', 'user_id')

    def get_status_display(self, obj):
        return obj.get_status_display()

