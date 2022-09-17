from django.db import models

class Writer(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
