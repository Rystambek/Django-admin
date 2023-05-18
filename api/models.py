from django.db import models

# Create your models here.

class Kompyuter(models.Model):
    name = models.CharField(max_length=50)
    brend = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    xotira = models.CharField(max_length=50)
    protsessor = models.CharField(max_length=50)
    about = models.TextField()


class Smartphones(models.Model):
    price = models.CharField(max_length=255)
    img_url = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)
    memory = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)

    def __str__(self):
        return self.name