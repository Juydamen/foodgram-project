from rest_framework import viewsets
from .models import User, Tag, Ingredient, RecipeList 
from .serializers import UserSerializer, TagSerializer, IngredientSerializer, RecipeListSerializer, ShoppingCartSerializer, FavoriteCartSerializer
from rest_framework.pagination import LimitOffsetPagination


class UserViewSet(viewsets.ModelViewSet):               # пользователи
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # pagination_class = LimitOffsetPagination


class TagViewSet(viewsets.ModelViewSet):                # теги
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class IngredientViewSet(viewsets.ModelViewSet):         # ингредиенты
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class RecipeListViewSet(viewsets.ModelViewSet):         # рецепты
    queryset = RecipeList.objects.all()
    serializer_class = RecipeListSerializer


class ShoppingCartViewSet(viewsets.ModelViewSet):       # список покупок
    queryset = RecipeList.objects.all()
    serializer_class = ShoppingCartSerializer


class FavoriteViewSet(viewsets.ModelViewSet):           # избранное
    queryset = RecipeList.objects.all()
    serializer_class = FavoriteCartSerializer
