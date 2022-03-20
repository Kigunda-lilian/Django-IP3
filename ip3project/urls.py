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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import re_path as url,include
from django.conf import settings
from django.conf.urls.static import static
from user import views as user_views
from rest_framework.urlpatterns import format_suffix_patterns




urlpatterns = [
     url(r'^admin/', admin.site.urls),
     url('register/',user_views.registration,name='register'),
     url('error/',user_views.registration,name='error'),
    
     url('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
      url('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
      url('profile/', user_views.user_profile,name='profile'),
      url("profile/update/", user_views.update_profile, name="update_profile"),
     url("api-auth/", include("rest_framework.urls")),
     url('',include('awards.urls')),
     
  # api
    url(r'^api/profile/$', user_views.ProfileList.as_view()),
  
  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns=format_suffix_patterns(urlpatterns)


