from django.core.management.base import BaseCommand, CommandError

from cocktails.models import Cocktail
from cocktails.models import Measure
from cocktails.models import Ingredient
from cocktails.models import Ingredients

class Command(BaseCommand):
    help = 'Migrate the ingredients and measures'

    def handle(self,*args,**options):
        try:
            for cocktail in Cocktail.objects.all():
                if cocktail.ingredient1 != None:
                    ingredients = Ingredients()
                    ingredients.cocktail = cocktail
                    ingredients.ingredient = Ingredient.objects.get(id=cocktail.ingredient1.id)
                    if cocktail.measure1 != None:
                        ingredients.measure = Measure.objects.get(id=cocktail.measure1.id)
                    ingredients.save()

                if cocktail.ingredient2 != None:
                    ingredients = Ingredients()
                    ingredients.cocktail = cocktail
                    ingredients.ingredient = Ingredient.objects.get(id=cocktail.ingredient2.id)
                    if cocktail.measure2 != None:
                        ingredients.measure = Measure.objects.get(id=cocktail.measure2.id)
                    ingredients.save()

                if cocktail.ingredient3 != None:
                    ingredients = Ingredients()
                    ingredients.cocktail = cocktail
                    ingredients.ingredient = Ingredient.objects.get(id=cocktail.ingredient3.id)
                    if cocktail.measure3 != None:
                        ingredients.measure = Measure.objects.get(id=cocktail.measure3.id)
                    ingredients.save()

                if cocktail.ingredient4 != None:
                    ingredients = Ingredients()
                    ingredients.cocktail = cocktail
                    ingredients.ingredient = Ingredient.objects.get(id=cocktail.ingredient4.id)
                    if cocktail.measure4 != None:
                        ingredients.measure = Measure.objects.get(id=cocktail.measure4.id)
                    ingredients.save()

                if cocktail.ingredient5 != None:
                    ingredients = Ingredients()
                    ingredients.cocktail = cocktail
                    ingredients.ingredient = Ingredient.objects.get(id=cocktail.ingredient5.id)
                    if cocktail.measure5 != None:
                        ingredients.measure = Measure.objects.get(id=cocktail.measure5.id)
                    ingredients.save()

                if cocktail.ingredient6 != None:
                    ingredients = Ingredients()
                    ingredients.cocktail = cocktail
                    ingredients.ingredient = Ingredient.objects.get(id=cocktail.ingredient6.id)
                    if cocktail.measure6 != None:
                        ingredients.measure = Measure.objects.get(id=cocktail.measure6.id)
                    ingredients.save()

                if cocktail.ingredient7 != None:
                    ingredients = Ingredients()
                    ingredients.cocktail = cocktail
                    ingredients.ingredient = Ingredient.objects.get(id=cocktail.ingredient7.id)
                    if cocktail.measure7 != None:
                        ingredients.measure = Measure.objects.get(id=cocktail.measure7.id)
                    ingredients.save()

                if cocktail.ingredient8 != None:
                    ingredients = Ingredients()
                    ingredients.cocktail = cocktail
                    ingredients.ingredient = Ingredient.objects.get(id=cocktail.ingredient8.id)
                    if cocktail.measure8 != None:
                        ingredients.measure = Measure.objects.get(id=cocktail.measure8.id)
                    ingredients.save()

                if cocktail.ingredient9 != None:
                    ingredients = Ingredients()
                    ingredients.cocktail = cocktail
                    ingredients.ingredient = Ingredient.objects.get(id=cocktail.ingredient9.id)
                    if cocktail.measure9 != None:
                        ingredients.measure = Measure.objects.get(id=cocktail.measure9.id)
                    ingredients.save()

                if cocktail.ingredient10 != None:
                    ingredients = Ingredients()
                    ingredients.cocktail = cocktail
                    ingredients.ingredient = Ingredient.objects.get(id=cocktail.ingredient10.id)
                    if cocktail.measure10 != None:
                        ingredients.measure = Measure.objects.get(id=cocktail.measure10.id)
                    ingredients.save()

                if cocktail.ingredient11 != None:
                    ingredients = Ingredients()
                    ingredients.cocktail = cocktail
                    ingredients.ingredient = Ingredient.objects.get(id=cocktail.ingredient11.id)
                    if cocktail.measure11 != None:
                        ingredients.measure = Measure.objects.get(id=cocktail.measure11.id)
                    ingredients.save()

                if cocktail.ingredient12 != None:
                    ingredients = Ingredients()
                    ingredients.cocktail = cocktail
                    ingredients.ingredient = Ingredient.objects.get(id=cocktail.ingredient12.id)
                    if cocktail.measure12 != None:
                        ingredients.measure = Measure.objects.get(id=cocktail.measure12.id)
                    ingredients.save()

                if cocktail.ingredient13 != None:
                    ingredients = Ingredients()
                    ingredients.cocktail = cocktail                
                    ingredients.ingredient = Ingredient.objects.get(id=cocktail.ingredient13.id)
                    if cocktail.measure13 != None:
                        ingredients.measure = Measure.objects.get(id=cocktail.measure13.id)
                    ingredients.save()

                if cocktail.ingredient14 != None:
                    ingredients = Ingredients()
                    ingredients.cocktail = cocktail
                    ingredients.ingredient = Ingredient.objects.get(id=cocktail.ingredient14.id)
                    if cocktail.measure14 != None:
                        ingredients.measure = Measure.objects.get(id=cocktail.measure14.id)
                    ingredients.save()

                if cocktail.ingredient15 != None:
                    ingredients = Ingredients()
                    ingredients.cocktail = cocktail
                    ingredients.ingredient = Ingredient.objects.get(id=cocktail.ingredient15.id)
                    if cocktail.measure15 != None:
                        ingredients.measure = Measure.objects.get(id=cocktail.measure15.id)
                    ingredients.save()

        except:
            raise CommandError('Error on migration of ingredients and measures');

        self.stdout.write('Migration successfull');