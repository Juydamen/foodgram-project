from django.urls import path, include
from .views import UserViewSet, TagViewSet, IngredientViewSet, RecipeListViewSet, ShoppingCartViewSet, FavoriteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'users', UserViewSet)                          # пользователи

router.register(r'tags', TagViewSet)                            # теги

router.register(r'recipes', RecipeListViewSet)                  # рецепты

router.register(r'recipes/(?<recipe_id>\d+)/shopping_cart',
                ShoppingCartViewSet,
                basename='shopping_cart')  # список покупок

router.register(r'recipes/(?<recipe_id>\d+)/favorite',
                FavoriteViewSet,
                basename='favorite')           # Избранное

router.register(r'ingredients', IngredientViewSet)


# router.register(r'posts/(?P<post_id>\d+)/comments',
#                 CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.token')),
]