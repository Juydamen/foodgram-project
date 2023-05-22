from rest_framework import serializers
from djoser.serializers import UserSerializer
from .models import User, Tag, Ingredient, RecipeList, Favorited, ShoppingCart


class UserSerializer(UserSerializer):                       # пользователи
    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name',
                  'last_name', 'is_subscribed')


class TagSerializer(UserSerializer):                        # +теги
    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'slug')


class IngredientSerializer(UserSerializer):                 # +ингредиенты
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'measurement_unit')


class RecipeListSerializer(UserSerializer):                 # +рецепты
    class Meta:
        model = RecipeList
        fields = ('id', 'tags', 'author', 'ingredients',
                  'is_favorited', 'is_in_shopping_cart',
                  'name', 'image', 'text', 'cooking_time')


class ShoppingCartSerializer(UserSerializer):               # список покупок
    class Meta:
        model = ShoppingCart
        fields = ('id', 'name', 'image', 'cooking_time')


class FavoriteCartSerializer(UserSerializer):               # избранные
    class Meta:
        model = Favorited
        fields = ('id', 'name', 'image', 'cooking_time')
