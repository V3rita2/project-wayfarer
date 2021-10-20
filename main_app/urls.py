from django.urls import path
from . import views

urlpatterns = [
    #path for home page
    path('', views.Home.as_view(), name="home"), 
    #path for profile page 
    path('profile/', views.Profile.as_view(), name="profile"),
    path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name="profile_update"),
    #path for single post about a park page
    #need to come back to update route
    path('posts/', views.Post.as_view(), name="posts"),
    #path to login- might need to update route later
    path('login/', views.Login.as_view(), name="login"),
    #path for user to sign-up/register
    path('signup/', views.Signup.as_view(), name="signup"),
    #path for creating a post about a park park
    path('create_post/', views.Create_Post.as_view(), name="create_post"),
]