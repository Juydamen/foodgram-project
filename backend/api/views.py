from rest_framework import viewsets
from users.models import User
from .serializers import UserCreateCustomSerializer, UserCustomSerializer
from .permissions import AuthorOrReadOnly, ReadOnly
# from rest_framework.pagination import LimitOffsetPagination


class UserCustomViewSet(viewsets.ModelViewSet):  # пользователи
    queryset = User.objects.all()
    serializer_class = UserCustomSerializer
    permission_classes = (AuthorOrReadOnly,)


class UserCreateCustomViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateCustomSerializer
    permission_classes = (AuthorOrReadOnly,)

    # def get_permissions(self):
    #     if self.action == 'retrieve':
    #         return (ReadOnly(),)
    #     return super().get_permissions()


# class TokenViewSet(viewsets.ModelViewSet):               # пользователи
#     queryset = User.objects.all()
#     serializer_class = TokenSerializer
    # authentication_classes = (SessionAuthentication,)

# class TagViewSet(viewsets.ModelViewSet):                # теги
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer


# class IngredientViewSet(viewsets.ModelViewSet):         # ингредиенты
#     queryset = Ingredient.objects.all()
#     serializer_class = IngredientSerializer


# class RecipeListViewSet(viewsets.ModelViewSet):         # рецепты
#     queryset = RecipeList.objects.all()
#     serializer_class = RecipeListSerializer


# class ShoppingCartViewSet(viewsets.ModelViewSet):       # список покупок
#     queryset = RecipeList.objects.all()
#     serializer_class = ShoppingCartSerializer


# class FavoriteViewSet(viewsets.ModelViewSet):           # избранное
#     queryset = RecipeList.objects.all()
#     serializer_class = FavoriteCartSerializer
