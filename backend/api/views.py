from rest_framework import viewsets
from users.models import User, Follow
from .serializers import UserCreateCustomSerializer, UserCustomSerializer, FollowSerialozer
from .permissions import AuthorOrReadOnly, ReadOnly
# from rest_framework.pagination import LimitOffsetPagination


class UserCustomViewSet(viewsets.ModelViewSet):  # пользователи
    queryset = User.objects.all()
    serializer_class = UserCustomSerializer
    permission_classes = (AuthorOrReadOnly,)
    # pagination_class = None
    # def get_permissions(self):
    #     if self.action == 'retrieve':
    #         return (ReadOnly(),)
    #     return super().get_permissions()


class UserCreateCustomViewSet(viewsets.ModelViewSet):  # для создания пользователя
    queryset = User.objects.all()
    serializer_class = UserCreateCustomSerializer
    permission_classes = (AuthorOrReadOnly,)
    # pagination_class = None

    # def get_permissions(self):
    #     if self.action == 'retrieve':
    #         return (ReadOnly(),)
    #     return super().get_permissions()


class SubscriptionViewSet(viewsets.ModelViewSet):  # для подписчика
    queryset = Follow.objects.all()
    serializer_class = FollowSerialozer
    # pagination_class = None

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

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
