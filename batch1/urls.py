"""batch1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import view, settings
#from day2 import views
from flyo import views
from.settings import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/',views.employeeList.as_view()),
    path('datapost/', views.employeeListPost.as_view()),
    #path('datadetail/<int:pk>/',views.detail),
    #path('',view.showpage,name='show'),
    #path('',include('tarvello.urls')),
    path('',include('fly.urls')),
    #path('day2/', include ('day2.urls'))

    #path('', include('addition.urls')),
    #path('',include('addition.urls')),
    #path('home/<int:pk>/', views.details, name='details'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout', views.logout, name='logout'),
    path('', views.home1, name='home1'),
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
