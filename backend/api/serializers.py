from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.core.files.base import ContentFile
from django.db import transaction
from djoser.serializers import UserSerializer, UserCreateSerializer
from users.models import (User,
                          Subscription)
from recipes.models import (Tag,
                            Ingredient,
                            Recipe,
                            Favorite,
                            ShoppingCart,
                            RecipeIngredient)
import base64
from api.utils import create_ingredients


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        return super().to_internal_value(data)


class UserCustomPostSerializer(UserCreateSerializer):
    """Сериализатор для получения, обновления, удаления токена"""

    class Meta:
        model = User
        fields = ('email', 'id',
                  'username', 'first_name',
                  'last_name', 'password')


class UserCustomGetSerializer(UserSerializer):
    """Сериализатор для отображения информации пользователях"""

    # новое поля - подписан ли текущий пользователь
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'id',
                  'username', 'first_name',
                  'last_name', 'is_subscribed')

    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        return (request.user.is_authenticated and
                Subscription.objects.filter(user=request.user,
                                            author=obj).exists())


class RecipeMinifiedSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения сокращённой информации о рецепте"""

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'image', 'cooking_time')


class SubscriptionGetSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения подписок пользователя"""

    is_subscribed = serializers.SerializerMethodField()
    recipes = serializers.SerializerMethodField()
    recipes_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name',
                  'last_name', 'is_subscribed', 'recipes', 'recipes_count')
        read_only_fields = ('email', 'username', 'first_name', 'last_name',
                            'is_subscribed', 'recipes', 'recipes_count')

    def get_recipes(self, obj):
        request = self.context.get('request')
        recipes_limit = None
        if request:
            recipes_limit = request.query_params.get('recipes_limit')
        recipes = obj.recipes.all()
        if recipes_limit:
            recipes = obj.recipes.all()[:int(recipes_limit)]
        return RecipeMinifiedSerializer(recipes,
                                        many=True,
                                        context={'request': request}).data

    def get_recipes_count(self, obj):
        return obj.recipes.count()


class SubscriptionPostSerializer(serializers.ModelSerializer):
    """Сериализатор для подписки на пользователя и отписки"""

    class Meta:
        model = Subscription
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Subscription.objects.all(),
                fields=('user', 'author'),
                message='Вы уже подписаны на этого пользователя'
            )
        ]

    # проверка валидатором
    def validate(self, data):
        request = self.context.get('request')
        if request.user == data['author']:
            raise serializers.ValidationError(
                'Нельзя подписываться на самого себя!'
            )
        return data

    # метод для отображения
    def to_representation(self, instance):
        request = self.context.get('request')
        return SubscriptionGetSerializer(instance.author,
                                         context={'request': request}).data


class TagSerializer(UserSerializer):
    """Сериализатор для отображения тегов"""

    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'slug')


class IngredientSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения ингредиентов"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'measurement_unit')


class IngredientGetSerializer(serializers.ModelSerializer):
    """Сериализатор для получения информации об ингредиентах.
    Используется при работе с рецептами"""

    id = serializers.IntegerField(source='ingredient.id', read_only=True)
    name = serializers.CharField(source='ingredient.name', read_only=True)
    measurement_unit = serializers.CharField(
        source='ingredient.measurement_unit',
        read_only=True)

    class Meta:
        model = RecipeIngredient
        fields = ('id', 'name', 'measurement_unit', 'amount')


class IngredientPostSerializer(serializers.ModelSerializer):
    """Сериализатор для добавления ингредиентов.
    Используется при работе с рецептами"""

    id = serializers.IntegerField()
    amount = serializers.IntegerField()

    class Meta:
        model = RecipeIngredient
        fields = ('id', 'amount')


class RecipeGetSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения информации о рецепте"""

    tags = TagSerializer(many=True, read_only=True)
    author = UserCustomGetSerializer(read_only=True)
    ingredients = IngredientGetSerializer(many=True,
                                          read_only=True,
                                          source='recipeingredients')
    is_favorited = serializers.SerializerMethodField()
    is_in_shopping_cart = serializers.SerializerMethodField()
    image = Base64ImageField(required=False)

    class Meta:
        model = Recipe
        fields = ('id', 'tags', 'author', 'ingredients',
                  'is_favorited', 'is_in_shopping_cart', 'name',
                  'image', 'text', 'cooking_time')

    def get_is_favorited(self, obj):                # метод
        request = self.context.get('request')
        return (request and request.user.is_authenticated
                and Favorite.objects.filter(user=request.user,
                                            recipe=obj).exists())

    def get_is_in_shopping_cart(self, obj):         # метод
        request = self.context.get('request')
        return (request and request.user.is_authenticated
                and ShoppingCart.objects.filter(user=request.user,
                                                recipe=obj).exists())


class RecipePostSerializer(serializers.ModelSerializer):
    """Сериализатор для добаления рецепта и обновление"""

    ingredients = IngredientPostSerializer(many=True,
                                           source='recipeingredients')
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(),
                                              many=True)
    image = Base64ImageField()

    class Meta:
        model = Recipe
        fields = ('ingredients', 'tags', 'image',
                  'name', 'text', 'cooking_time')

    def validate(self, data):
        ingredients_list = []
        for ingredient in data.get('recipeingredients'):
            if ingredient.get('amount') <= 0:
                raise serializers.ValidationError(
                    'Количество не может быть меньше 1'
                )
            ingredients_list.append(ingredient.get('id'))
        if len(set(ingredients_list)) != len(ingredients_list):
            raise serializers.ValidationError(
                'Вы пытаетесь добавить в рецепт два одинаковых ингредиента')
        return data

    @transaction.atomic
    def create(self, validated_data):
        request = self.context.get('request')
        ingredients = validated_data.pop('recipeingredients')
        tags = validated_data.pop('tags')
        recipe = Recipe.objects.create(author=request.user, **validated_data)
        recipe.tags.set(tags)
        create_ingredients(ingredients, recipe)
        return recipe

    @transaction.atomic
    def update(self, instance, validated_data):
        ingredients = validated_data.pop('recipeingredients')
        tags = validated_data.pop('tags')
        instance.tags.clear()
        instance.tags.set(tags)
        RecipeIngredient.objects.filter(recipe=instance).delete()
        super().update(instance, validated_data)
        create_ingredients(ingredients, instance)
        instance.save()
        return instance

    def to_representation(self, instance):
        request = self.context.get('request')
        return RecipeGetSerializer(
            instance,
            context={'request': request}).data


class FavoriteSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения избранных рецептов"""

    class Meta:
        model = Favorite
        fields = '__all__'              # получаем все поля
        validators = [
            UniqueTogetherValidator(
                queryset=Favorite.objects.all(),
                fields=('user', 'recipe'),
                message='Рецепт уже добавлен в избранное'
            )
        ]

    def to_representation(self, instance):
        request = self.context.get('request')
        return RecipeMinifiedSerializer(instance.recipe,
                                        context={'request': request}).data


class ShoppingCartSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения списков покупок"""

    class Meta:
        model = ShoppingCart
        fields = '__all__'          # получаем все поля
        validators = [
            UniqueTogetherValidator(
                queryset=ShoppingCart.objects.all(),
                fields=('user', 'recipe'),
                message='Рецепт уже добавлен в список покупок'
            )
        ]

    def to_representation(self, instance):
        request = self.context.get('request')
        return RecipeMinifiedSerializer(instance.recipe,
                                        context={'request': request}).data
