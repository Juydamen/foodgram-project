from django.contrib.auth import models
from django.db import models


class User(models.AbstractUser):            # +Модель пользователя
    email = models.CharField(max_length=254)
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_subscribed = models.BooleanField(blank=True)


class Tag(models.Model):                    # +Модель тэга
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=7)
    slug = models.CharField(max_length=200, unique=True)


class Ingredient(models.Model):             # +Модель ингредиента
    name = models.CharField(max_length=200)
    measurement_unit = models.CharField(max_length=200)


class RecipeList(models.Model):             # +Модель рецепта
    tags = models.ForeignKey(Tag,
                             related_name='recipelists',
                             on_delete=models.CASCADE)
    author = models.ForeignKey(User,
                               related_name='recipelists',
                               on_delete=models.CASCADE)
    ingredients = models.ForeignKey(Ingredient,
                                    related_name='recipelists',
                                    on_delete=models.CASCADE)
    # is_favorited =
    # is_in_shopping_cart =
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='api/image/',
                              null=True,
                              blank=True)
    text = models.TextField()
    cooking_time = models.IntegerField()
