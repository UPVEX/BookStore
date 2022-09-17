from django.contrib import admin
from .models import Book

class AddBook(admin.ModelAdmin):
	list_display = ['name', 'price', 'created', 'updated']

admin.site.register(Book, AddBook)
