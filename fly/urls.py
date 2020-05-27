from django.contrib import admin
from django.urls import path,include

from flyo.views import ActivateAccount
from paygate.views import paymentMode
from.import views
urlpatterns = [
    path('',views.home1,name='home1'),
    path('htmlfile',views.htmlfile,name='htmlfile'),
    path('aboutt',views.aboutt,name='aboutt'),
    path('contactus',views.contactus,name='contactus'),
    path('servicess',views.servicess,name='servicess'),
    path('adven', views.adven, name='adven'),
    path('couple', views.couple, name='couple'),
    path('national', views.national, name='national'),
    path('religious', views.religious, name='religious'),
    path('paymentMode/', paymentMode, name='handle'),
    path('hotel', views.hotel, name='hotel'),
    path('reservations', views.reservations, name='reservations'),
    path('car', views.car, name='car'),
    path('flight', views.flight, name='flight'),
    path('train', views.train, name='train'),
    path('next', views.next, name='next'),
    path('next2', views.next2, name='next2'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('paytm',views.paytm, name='paytm'),
    path('water',views.water, name='water'),
    path('viewdetails',views.viewdetails, name='viewdetails'),

]
