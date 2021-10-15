from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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
    
#sign-up view- Mehari is working on sign-up page
class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)