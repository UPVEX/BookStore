from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Writer(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    enable = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return self.name
    