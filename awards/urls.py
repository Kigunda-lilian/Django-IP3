"""ip3project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import re_path as url,include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin



urlpatterns = [

    url(r'^$',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    url('home/', views.index, name='home'),
    url('search/', views.search_results,name='search_results'),
    
    url("project/save/", views.save_project, name="save_project"),
    url("project/<int:project_id>/", views.project_details, name="project_details"),
    url("project/delete/<int:id>/", views.delete_project, name="delete_project"),
    url("project/rate/<int:id>/", views.rate_project, name="rate_project"),
    url("search/", views.search_results, name="search_project"),
    
    # api
  
    url(r'^api/project/$', views.ProjectList.as_view()),

    
    ]
    
  
 

   
    
    

