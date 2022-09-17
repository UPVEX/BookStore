from django.db import models
from writer.models import Writer
from category.models import Category

class Book(models.Model):
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    enable = models.BooleanField(default=False)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
