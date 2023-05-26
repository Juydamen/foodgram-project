from django.urls import path, include
from .views import UserCustomViewSet, UserCreateCustomViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()

router.register(r'', UserCustomViewSet)
router.register(r'', UserCreateCustomViewSet)




# router.register(r'login', TokenViewSet)                  # получение токена
# router.register(r'tags', TagViewSet)                            # теги
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
    # path('', include(router.urls)),
    path('', include('djoser.urls')),  # Работа с пользователями.
    path('auth/', include('djoser.urls.authtoken')),  # Работа с токенами.

]


#  urlpatterns += [
#     path('auth/token/', views.obtain_auth_token),
#     path('set_password/', views.obtain_auth_token)
# ]