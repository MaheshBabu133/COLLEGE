from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class College(models.Model):

    collegename = models.CharField(max_length = 150,primary_key = True)
    established = models.IntegerField()
    location = models.CharField(max_length = 150)
    website = models.URLField(max_length = 200)
    cimage = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    branch = models.IntegerField()
    course = models.CharField(max_length = 100)
    fees = models.IntegerField()
    description = models.TextField(default ='college')
    def __str__(self):
        return self.collegename
        
