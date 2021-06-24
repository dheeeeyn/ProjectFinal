from django.conf.urls import url 
from VApp import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.Home, name='home'),
    url(r'^VApp/donate$', views.Donate, name='donate'),
    url(r'^VApp/volunteer$', views.Volunteer, name='volunteer'),
    url(r'^VApp/profile$', views.Profile, name='profile'),
    url(r'^VApp/login$', views.Login, name='login'),
    url('admin/', admin.site.urls),
]

# urlpatterns = [
#     url(r'^$', views.VolunteerForm, name='volunteerform'),
#     url(r'^VApp/(\d+)/$', views.ViewList, name='viewList'),
#     url(r'^VApp/newList_url$', views.NewList, name='newList'),
#     url(r'^VApp/(\d+)/addItem$', views.VolList, name='additem'),
#     url('admin/', admin.site.urls),
# ]


"""ProjectFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
