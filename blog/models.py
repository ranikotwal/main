from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

