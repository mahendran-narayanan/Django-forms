from django.db import models

# Create your models here.

class Data(models.Model):
	name = models.CharField(max_length=25)
	age = models.IntegerField()
	sal = models.IntegerField(default=5000)