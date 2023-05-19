from django.db import models
from django.contrib.auth import models


class User(models.AbstractUser):        # Модель пользователя
    pass


class Tag(models.Model):           # Модель тэга
    pass


class Recipe(models.Model):         # Модель рецепта
    pass


class ShoppingCart(models.Model):       # Модель списока покупок
    pass


class Favorite(models.Model):       # Модель избранного
    pass


class Subscribe(models.Model):          # Модель подписок
    pass


class Ingredient(models.Model):          # Модель ингредиента
    pass