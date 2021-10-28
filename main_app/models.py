from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# model for the city pages, will be hardcoded
class City(models.Model):

    name = models.CharField(max_length=256)
    # Will also need a route to upload to
    image = models.ImageField(upload_to=None)
    description = models.TextField(max_length=9999)
    
    def __str__(self):
        return self.name

#model for parks
class Park(models.Model):

    name = models.CharField(max_length=256)
    #upload_to will have to have a route dedicated to it, possibly have a few for posting.
    image = models.CharField(max_length=500)
    #no character limit to description, front end will cut off 1000 or more unless clicked on
    description = models.TextField(max_length=9999)
    created_at = models.DateTimeField(auto_now_add=True)
    # allows a park to be connected to a city, all parks from a city will be deleted if the city is deleted
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="parks")
    # Keeps track of the user that makes the post about the park
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# A user model that calls the Django aouth user as a one to one, so users can have and change their locations, screen name, etc.
class Person(models.Model):
    #when user is deleted, delete the person attached to it
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #display name will default to User.name, but can be changed without altering login credentials
    display_name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
