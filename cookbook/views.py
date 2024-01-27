from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Recipe, Recipe_product
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F

# Create your views here.
def add_product_to_recipe(request, recipe_id, product_id, weight):
    if request.method == "GET":
        try:
            # Проверяем наличие рецептов с продуктами в БД
            recipe_product = Recipe_product.objects.get(recipe_id=recipe_id, product_id=product_id)
            recipe_product.weight = weight
            recipe_product.save()
            return HttpResponse(f"Объект {recipe_product} обновлен")
        except ObjectDoesNotExist:
            try:
                # Проверяем наличие рецептов и продуктов в БД
                recipe = Recipe.objects.get(id=recipe_id)
                product = Product.objects.get(id=product_id)
                # Создаем новую запись
                recipe_product = Recipe_product(
                    recipe=recipe, product=product, weight=weight
                )
                recipe_product.save()
                return HttpResponse(f"Объект {recipe_product} создан")
            except ObjectDoesNotExist:
                return HttpResponse(f"Объект не может быть создан")
    return HttpResponse("Метод не поддерживается")


def cook_recipe(request, recipe_id):
    if request.method == "GET":
        products = Recipe_product.objects.filter(recipe=recipe_id).values("product_id")
        if products:
            for product in products:
                Product.objects.filter(id=product["product_id"]).update(dish_counter=F("dish_counter") + 1)
            return HttpResponse("Счетчик блюд у продуктов увеличен")
        else:
            return HttpResponse("Продукты не найдены")
    return HttpResponse("Метод не поддерживается")


def show_recipes_without_product(request, product_id):
    if request.method == "GET":
        recipe_product = Recipe_product.objects.filter(product=product_id).values("recipe__title")
        recipes = Recipe.objects.exclude(title__in=recipe_product) | Recipe.objects.filter(title__in=recipe_product.filter(weight__lt=10))
        return render(request, "cookbook/table_recipe.html", {'recipes':recipes})
    return HttpResponse("Метод не поддерживается")