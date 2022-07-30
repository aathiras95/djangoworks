from django.db import models

# Create your models here
class Products(models.Model):
    name=models.CharField(max_length=120)
    spec=models.CharField(max_length=120)
    price=models.PositiveIntegerField()

    def __str__(self):
        return self.name