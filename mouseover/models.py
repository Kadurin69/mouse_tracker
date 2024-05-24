from django.db import models

# Create your models here.
class MouseData(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    image_location = models.CharField(max_length=100)