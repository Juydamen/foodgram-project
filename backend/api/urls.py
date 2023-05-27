from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()

router.register(r'', UserCustomViewSet)  # получение пользователей
router.register(r'', UserCreateCustomViewSet)  # получение токенов
router.register(r'subscriptions/', FollowViewSet)
router.register(r'tags/', TagViewSet)

# router.register(r'users/(?P<username_id>\d+)subscribe/',
#                 FollowViewSet, basename='subscribe')  # ссылка для подписчиков





# router.register(r'recipes', RecipeListViewSet)                  # рецепты
# router.register(r'recipes/(?<recipe_id>\d+)/shopping_cart',
#                 ShoppingCartViewSet,
#                 basename='shopping_cart')  # список покупок
# router.register(r'recipes/(?<recipe_id>\d+)/favorite',
#                 FavoriteViewSet,
#                 basename='favorite')           # Избранное
# router.register(r'ingredients', IngredientViewSet)
# router.register(r'posts/(?P<post_id>\d+)/comments',
#                 CommentViewSet, basename='comments')

urlpatterns = [
    path('users', include(router.urls)),
    path('', include('djoser.urls')),  # Работа с пользователями.
    path('auth/', include('djoser.urls.authtoken')),  # Работа с токенами.

]


urlpatterns += [
    # path('', include('djoser.urls')),  # Работа с пользователями.
    # path('auth/', include('djoser.urls.authtoken')),  # Работа с токенами.
]