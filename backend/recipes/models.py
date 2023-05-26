from django.db import models
from users.models import User


class Tag(models.Model):                    # +Модель тэга
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=7)
    slug = models.CharField(max_length=200, unique=True)


class Ingredient(models.Model):             # +Модель ингредиента
    name = models.CharField(max_length=200)
    measurement_unit = models.CharField(max_length=200)


class Recipe(models.Model):             # +Модель рецепта
    tags = models.ManyToManyField(Tag,
                                  related_name='recipelists')

    author = models.ForeignKey(User,
                               related_name='recipelists',
                               on_delete=models.CASCADE)

    ingredients = models.ManyToManyField(Ingredient,
                                         related_name='recipelists')

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='api/image/',
                              null=True,
                              blank=True)
    text = models.TextField()
    cooking_time = models.IntegerField()
    publication_date = models.DateTimeField(auto_now_add=True)


class Favorite(models.Model):
    author = models.ForeignKey(User,
                               related_name='favorite_author',
                               on_delete=models.CASCADE)    
    recipe = models.ForeignKey(Recipe,
                               related_name='favorite_recipe',
                               on_delete=models.CASCADE)


class Shopping_cart(models.Model):
    author = models.ForeignKey(User,
                               related_name='shopping_author',
                               on_delete=models.CASCADE)

    recipe = models.ForeignKey(Recipe,
                               related_name='shopping_recipe',
                               on_delete=models.CASCADE)
