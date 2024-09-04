from django.contrib import admin
from .models import Category, Meal, Order, OrderItem, Basket, Requirements, Vacancy, News, About, Branches, Employee


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register([Meal, Order, OrderItem, Basket, Requirements, Vacancy, News, About, Branches, Employee])
