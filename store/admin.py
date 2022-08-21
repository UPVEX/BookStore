from django.contrib import admin
from .models import Category, Writer, Book


class AddCategory(admin.ModelAdmin):
	list_display = ['name']

admin.site.register(Category, AddCategory)


class AddWriter(admin.ModelAdmin):
	list_display = ['name']

admin.site.register(Writer, AddWriter)


class AddBook(admin.ModelAdmin):
	list_display = ['name', 'price', 'created', 'updated']

admin.site.register(Book, AddBook)
