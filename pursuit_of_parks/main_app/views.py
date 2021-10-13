from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
#homepage route
class Home(TemplateView):
    template_name = "home.html"
