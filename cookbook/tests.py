from django.test import TestCase

from cookbook.models import Recipe, Recipe_product, Product

# Create your tests here.
class ModelTest(TestCase):
    def add_product_to_recipe():
        recipe = Recipe.objects.get(id=1)
        product = Product.objects.get(id=1)
        recipe_product = Recipe_product(recipe=recipe, product=product, weight)
        recipe_product.recipe = recipe
        recipe_product.product = product
        recipe_product.weight = 400
        print(recipe_product)
        print(recipe_product.recipe)
        print(recipe_product.product)
        print(recipe_product.weight)
