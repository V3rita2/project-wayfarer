from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
#homepage 
class Home(TemplateView):
    template_name = "home.html"

#profile 
class Profile(TemplateView):
    template_name = "profile.html"
