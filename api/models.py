from django.db import models

# Create your models here.

class Kompyuter(models.Model):
    name = models.CharField(max_length=50)
    brend = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    xotira = models.CharField(max_length=50)
    protsessor = models.CharField(max_length=50)
    about = models.TextField()
