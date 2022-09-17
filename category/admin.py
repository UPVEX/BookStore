from django.contrib import admin
from .models import Category

class AddCategory(admin.ModelAdmin):
	list_display = ['name']

admin.site.register(Category, AddCategory)
