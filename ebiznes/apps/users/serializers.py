from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True, allow_null=False)
    last_name = serializers.CharField(required=True, allow_null=False)

    def save(self, request):
        user = super().save(request)

        user.first_name = request.data['first_name']
        user.last_name = request.data['last_name']

        user.save()

        return user
