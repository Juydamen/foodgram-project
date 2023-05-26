from rest_framework import serializers
from djoser.serializers import UserSerializer, UserCreateSerializer
from users.models import User, Follow
# from recipes.models import Tag, Ingredient, RecipeList


class UserCreateCustomSerializer(UserCreateSerializer):  # Пользователь для создания токена
    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name', 'last_name',
                  'password')


class UserCustomSerializer(UserSerializer):  # Пользователь для отображения
    # is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'id',
                  'username', 'first_name',
                  'last_name', 'is_subscribed')

    # def get_is_subscribed(self, obj):
    #     return get_boolean(self, Follow, obj)


class FollowSerialozer(serializers.ModelSerializer):  # Подписчики
    user = serializers.SlugRelatedField(
        slug_field='username', read_only=True,
        default=serializers.CurrentUserDefault())

    author = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = ('user', 'author')
