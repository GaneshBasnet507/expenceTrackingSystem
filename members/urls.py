from django.urls import path
from .import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
     path('members/register/', views.register, name='register'),
     path('members/loogin/', views.login, name='login'),
      path('userdashboard/', views.userdashboard, name='userdashboard'),
      path('register/', views.register, name='register'),
       path('addexpence/', views.addexpence, name='addexpence'),
]           