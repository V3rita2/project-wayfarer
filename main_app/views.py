from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView
from sre_compile import _SUCCESS_CODES
from .models import City, Park, Person
from django.urls import reverse

# Create your views here.
# homepage view


class Home(TemplateView):
    template_name = "home.html"


# about view
class About(TemplateView):
    template_name = "about.html"

# profile view


class Profile(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["parks"] = Park.objects.all()
        return context



# single post view for parks
class Post(TemplateView):
    template_name = "posts.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context["parks"] = Park.objects.all()
        return context

    







class Create_Post(CreateView):
    model = Park
    fields = ["name", "image", "description", "city", "user"]
    template_name = "create_post.html"
    success_url = "/cities/1/"

    # def get_success_url(self):
    #     return reverse('city_detail', kwargs={'pk': City.pk})

# edit post view- front end needs to create post_update.html


class PostUpdate(UpdateView):
    model = Park
    fields = ["name", "image", "description", "city", "user"]
    template_name = "post_update.html"
    success_url = "/cities/"
    # front end needs to create post_detail.html

    # def get_success_url(self):
    #     return reverse('city_detail', kwargs={'pk': self.object.pk})

# delete post vire- front ends needs to create post_delete_confirmation.html or actually not sure how this would work since we're using modal for pop-up??


class PostDelete(DeleteView):
    model = Park
    template_name = "post_delete_confirmation.html"
    success_url = "/cities/"


# login view
class Login(TemplateView):
    template_name = "login.html"

# sign-up view- Mehari is working on sign-up page


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
# signup 2 electric boogaloo


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["citys"] = City.objects.all()
        return context

# city detail view


class CityDetail(DetailView):
    model = City
    template_name = "city_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["parks"] = Park.objects.all()
        return context


class Park_Detail(DetailView):
    model = Park
    template_name = "posts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        return context
