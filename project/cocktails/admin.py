from django.contrib.admin import register, ModelAdmin

from cocktails.models import Cocktail, Ingredient, Glass, Category, Measure


@register(Glass)
class DrinkAdmin(ModelAdmin):
    pass


@register(Category)
class CategoryAdmin(ModelAdmin):
    pass


@register(Ingredient)
class IngredientAdmin(ModelAdmin):
    pass


@register(Measure)
class MeasureAdmin(ModelAdmin):
    pass


@register(Cocktail)
class CocktailAdmin(ModelAdmin):
    pass


