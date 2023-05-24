from rest_framework import serializers
from djoser.serializers import UserSerializer
from users.models import User


class UserCustomSerializer(UserSerializer):                       # пользователи

    class Meta:
        model = User
        fields = ('email',
                  'id',
                  'username',
                  'first_name',
                  'last_name',
                  'is_subscribed')


# class TokenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email', 'password']
#         # extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User(
#             email=validated_data['email'],
#             password=validated_data['password']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
