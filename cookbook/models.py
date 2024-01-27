from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name="Наименование")
    dish_counter = models.IntegerField(verbose_name="Использовано в блюдах")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.title}"


class Recipe(models.Model):
    title = models.CharField(max_length=50, verbose_name="Наименование")
    products = models.ManyToManyField(Product, through="Recipe_product")

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return f"{self.title}"


class Recipe_product(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name="Рецепт")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    weight = models.IntegerField(null=True, blank=True, verbose_name="Вес")

    class Meta:
        verbose_name = "Продукты к рецептам"
        verbose_name_plural = "Список продуктов"

    def __str__(self):
        return f"{self.recipe.title}"
