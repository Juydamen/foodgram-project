from rest_framework import serializers
from djoser.serializers import UserSerializer
from .models import User


class UserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name',
                  'last_name', 'is_subscribed')
