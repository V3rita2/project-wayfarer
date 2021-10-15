from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# model for the city pages, will be hardcoded
class City(models.Model):

    name = models.CharField(max_length=256)
    # Will also need a route to upload to
    image = models.ImageField(upload_to=None)
    description = models.TextField

#model for parks
class Park(models.Model):

    name = models.CharField(max_length=256)
    #upload_to will have to have a route dedicated to it, possibly have a few for posting.
    image = models.ImageField(upload_to=None)
    #no character limit to description, front end will cut off 1000 or more unless clicked on
    description = models.TextField
    created_at = models.DateTimeField(auto_now_add=True)
    # allows a park to be connected to a city, all parks from a city will be deleted if the city is deleted
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    # Keeps track of the user that makes the post about the park
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# Model for Current City. Needs to be able to change by the user.
class CurrentCity(models.Model):
    
    name = models.