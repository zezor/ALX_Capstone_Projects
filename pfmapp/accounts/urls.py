from django.urls import path
from  . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('user_details/', views.UserDetailView.as_view(), name='user_details'),
    path('login/', views.LoginView.as_view(), name='login'),


]