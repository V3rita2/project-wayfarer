from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView
from sre_compile import _SUCCESS_CODES
from .models import City, Park, Person

# Create your views here.
#homepage view 
class Home(TemplateView):
    template_name = "home.html"

#profile view
class Profile(TemplateView):
    template_name = "profile.html"
    

#single post view for parks
class Post(TemplateView):
    template_name = "posts.html"
   

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
#signup 2 electric boogaloo
class UserLink(CreateView):
    model = Person
    fields = ['display_name', 'location']
    template_name = 'user_link.html'
    success_url = '/profile'

class ProfileUpdate(UpdateView):
    model = Person
    fields = ['display_name', 'location']
    template_name = 'profile_update.html'
    success_url = '/profile/'



# city views, for list and detail, list first, then detail
class CityList(TemplateView):
    template_name = 'city_list.html'

#city detail view
class CityDetail(DetailView):
    model = City
    template_name = "city_detail.html"