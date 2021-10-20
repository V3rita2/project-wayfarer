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
    #paths for user to sign-up/register
    path('signup/', views.Signup.as_view(), name="signup"),
    path('signup/userlink', views.UserLink.as_view(), name="user_link"),
    #path for city list page
    path('cities/', views.CityList.as_view(), name='cities'),
    #path for single city page
    path('cities/<int:pk>', views.CityDetail.as_view(), name='city_detail'),
    
]