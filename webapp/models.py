from django.db import models
# from django.urls import reverse

# Create your models here.

class BeerDB(models.Model):
    name=models.CharField(max_length=100)
    taste=models.CharField(max_length=100)
    color=models.CharField(max_length=50)
    price=models.FloatField()

    # def get_absolute(self):
    #     return reverse('abs',kwargs={'pk':self.pk})
    #
