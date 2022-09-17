from django.contrib import admin
from .models import Writer


class AddWriter(admin.ModelAdmin):
	list_display = ['name']

admin.site.register(Writer, AddWriter)