from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
#homepage view 
class Home(TemplateView):
    template_name = "home.html"

#profile view
class Profile(TemplateView):
    template_name = "profile.html"

#single post view for parks
class Post(TemplateView):
    template_name = "post.html"

#login view
class Login(TemplateView):
    template_name = "login.html"