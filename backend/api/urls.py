from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import (UserSubscribeView,
                       UserSubscriptionsViewSet,
                       TagViewSet,
                       IngredientViewSet,
                       RecipeViewSet)

router = DefaultRouter()

router.register(r'tags', TagViewSet, basename='tags')
router.register(r'ingredients', IngredientViewSet, basename='ingredients')
router.register(r'recipes', RecipeViewSet, basename='recipes')

urlpatterns = [
    # получение подписок пользователя
    path('users/subscriptions/',
         UserSubscriptionsViewSet.as_view({'get': 'list'})),
    # создание подписки
    path('users/<int:user_id>/subscribe/', UserSubscribeView.as_view()),

    path('', include(router.urls)),
    # работа с пользователями
    path('', include('djoser.urls')),
    # работа с токенами
    path('auth/', include('djoser.urls.authtoken')),
]
