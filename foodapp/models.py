from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=15)
    price = models.IntegerField()

    def __str__(self):
        return self.name