from django.contrib import admin
from recipes.models import (Tag,
                            Ingredient,
                            Recipe,
                            Favorite,
                            ShoppingCart,
                            RecipeIngredient)


class TagAdmin(admin.ModelAdmin):
    """Отображение тегов в админке с 4 полями"""

    list_display = ('id',
                    'name',
                    'color',
                    'slug')


class IngredientAdmin(admin.ModelAdmin):
    """Отображение ингредиентов в админке с 3 полями"""

    list_display = ('id',
                    'name',
                    'measurement_unit')


class RecipeIngredientInline(admin.TabularInline):
    """Отображение рецепта в админке с полями
    прописанными в моделе recipe.models"""

    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    """Отображение рецептов в админке с:
    - полями list_display в таблице
    - поисковые поля search_fields
    - поля фильтрации list_filter
    - поле линия inlines"""

    list_display = ('id', 'name', 'author',
                    'favorites_amount',
                    'publication_date')
    search_fields = ('name', 'author')
    list_filter = ('name', 'author', 'tags')

    inlines = [
        RecipeIngredientInline,
    ]

    def favorites_amount(self, obj):
        return obj.favorites.count()


class RecipeIngredientAdmin(admin.ModelAdmin):
    """Отображение рецепта с ингредиентами в админке с 4 полями"""

    list_display = ('id', 'recipe', 'ingredient', 'amount')


class FavoriteAdmin(admin.ModelAdmin):
    """Отображение избранных в админке с 3 полями"""

    list_display = ('id',
                    'author',
                    'recipe')


class Shopping_cartAdmin(admin.ModelAdmin):
    """Отображение списка покупок в админке с 3 полями"""

    list_display = ('id',
                    'author',
                    'recipe')


admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(ShoppingCart, Shopping_cartAdmin)
