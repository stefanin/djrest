from django.db import models

# Create your models here.

class dafare(models.Model):
    titolo= models.CharField(max_length=256)
    fatto= models.BooleanField()

