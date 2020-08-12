from django.db import models
from django.db import models
# Create your models here.

class Tweet(models.Model):
    date = models.DateField()
    tweet = models.CharField(max_length=300)
    
