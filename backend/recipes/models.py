from django.db import models
from users.models import User
from django.core.validators import MinValueValidator


class Tag(models.Model):                # Модель тэга
    # название тега
    name = models.CharField(max_length=200, unique=True)
    # цвет тега
    color = models.CharField(max_length=7, unique=True)
    # слаг тега
    slug = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Тег'            # удобочитаемое имя модели
        verbose_name_plural = 'Теги'    # переименовать в админке

    def __str__(self):
        return self.name


class Ingredient(models.Model):         # Модель ингредиента
    # име ингредиента
    name = models.CharField(max_length=200)
    # единица измерения
    measurement_unit = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Ингредиент'              # удобочитаемое имя модели
        verbose_name_plural = 'Ингредиенты'      # переименовать в админке

    def __str__(self):
        return self.name


class Recipe(models.Model):             # Модель рецепта
    # тег рецепта
    tags = models.ManyToManyField(Tag,
                                  verbose_name='Теги')
    # автор рецепта
    author = models.ForeignKey(User,
                               related_name='recipelists',
                               on_delete=models.CASCADE,
                               verbose_name='Автор',)
    # ингредиенты
    ingredients = models.ManyToManyField(Ingredient,
                                         related_name='recipelists')
    # название рецепта
    name = models.CharField(max_length=200)
    # изображение рецепта
    image = models.ImageField(upload_to='api/image/',
                              null=True,
                              blank=True)
    # описание рецепта
    text = models.TextField()
    # время приготовления рецепта
    cooking_time = models.IntegerField()
    # дата и время публикации рецепта
    publication_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-publication_date']
        verbose_name = 'Рецепт'                 # удобочитаемое имя модели
        verbose_name_plural = 'Рецепты'         # переименовать в админке

    def __str__(self):
        return self.name


class Favorite(models.Model):           # Модель избранное
    # автор
    author = models.ForeignKey(User,
                               related_name='favorite_author',
                               on_delete=models.CASCADE,
                               verbose_name='Пользователь')
    # рецепт добавляемый в избранное
    recipe = models.ForeignKey(Recipe,
                               related_name='favorite_recipe',
                               on_delete=models.CASCADE,
                               verbose_name='Рецепт')

    class Meta:                     # ????????????
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'recipe'],
                name='unique_author_recipe_favorite'
            )
        ]
        verbose_name = 'Избранное'              # удобочитаемое имя модели
        verbose_name_plural = 'Избранное'       # переименовать в админке

    def __str__(self):
        return (f'{self.author.username}'
                f'добавил {self.recipe.name} в избраннное.')


class ShoppingCart(models.Model):       # Модкль списка покупок
    # автор
    author = models.ForeignKey(User,
                               related_name='shopping_author',
                               on_delete=models.CASCADE)
    # рецепт добавляемый в список покупок
    recipe = models.ForeignKey(Recipe,
                               related_name='shopping_recipe',
                               on_delete=models.CASCADE)

    class Meta:                     # ??????????????
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'recipe'],
                name='unique_author_recipe_shopping_cart'
            )
        ]
        verbose_name = 'Список покупок'              # удобочитаемое имя модели
        verbose_name_plural = 'Списоки покупок'       # переименовать в админке

    def __str__(self):
        return (f'{self.author.username}'
                f'добавил {self.recipe.name} в список покупок.')


class RecipeIngredient(models.Model):   # Модель рецепта с ингредиентами
    # рецепт
    recipe = models.ForeignKey(Recipe,
                               related_name='recipeingredients',
                               on_delete=models.CASCADE,
                               verbose_name='Рецепт')
    # ингредиент который входят в рецепт
    ingredient = models.ForeignKey(Ingredient,
                                   related_name='recipeingredients',
                                   on_delete=models.CASCADE,
                                   verbose_name='Ингредиент')
    # количество ингредиента в рецепет
    amount = models.IntegerField(validators=[MinValueValidator(
        1, 'Количество ингредиентов не может быть меньше 1')]
    )

    class Meta:
        # удобочитаемое имя модели
        verbose_name = 'Ингредиент в рецепте'
        # переименовать в админке
        verbose_name_plural = 'Ингредиенты в рецепте'
