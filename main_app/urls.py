from django.urls import path
from . import views

urlpatterns = [
    #path for home page
    path('', views.Home.as_view(), name="home"), 
    #path for profile page 
    path('profile/', views.Profile.as_view(), name="profile"),
    
    #path for single post about a park page
    #need to come back to update route
    path('park/', views.Post.as_view(), name="post")
]