from django.contrib import admin
from .models import Product, Recipe, Recipe_product

# Register your models here.
class Recipe_productInline(admin.TabularInline):
    model = Recipe_product

class RecipeAdmin(admin.ModelAdmin):
    inlines = [Recipe_productInline]

admin.site.register(Product) 
admin.site.register(Recipe, RecipeAdmin)
