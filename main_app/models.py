from django.db import models

# Create your models here.

#model for parks
class Park(models.Model):

    name = models.CharField(max_length=256)
    #upload_to will have to have a route dedicated to it, possibly have a few for posting.
    image = models.ImageField(upload_to=None)
    #no character limit to description, front end will cut off 1000 or more unless clicked on
    description = models.TextField
    created_at = models.DateTimeField(auto_now_add=True)
