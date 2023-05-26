from django.contrib import admin
from recipes.models import Tag, Ingredient, Recipe, Favorite, Shopping_cart


class TagAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'color',
                    'slug')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'measurement_unit')


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'get_tags',
                    'author',
                    'get_ingredients',
                    'name',
                    'image',
                    'text',
                    'cooking_time',
                    'publication_date')

    def get_tags(self, obj):
        return "\n".join([p.tags for p in obj.tags.all()])

    def get_ingredients(self, obj):
        return "\n".join([p.ingredients for p in obj.ingredients.all()])


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'author',
                    'recipe')


class Shopping_cartAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'author',
                    'recipe')


admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Shopping_cart, Shopping_cartAdmin)