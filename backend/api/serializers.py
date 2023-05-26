from rest_framework import serializers
from djoser.serializers import UserSerializer, UserCreateSerializer
from users.models import User


class UserCreateCustomSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name', 'last_name',
                  'password')


class UserCustomSerializer(UserSerializer):
    # is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name', 'last_name') #'is_subscribed'

    # def get_is_subscribed(self, obj):
    #     return get_boolean(self, Follow, obj)
