from __future__ import unicode_literals
from django.db import models
# Create your models here.
class  data(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    username = models.CharField(max_length=20)
    password = models.TextField()
    confirm_password = models.TextField()
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    birth = models.CharField(max_length=15)
    mobile_number = models.CharField(max_length=10)

class destinationss(models.Model):
    name_of_destination = models.CharField(max_length=30)
    profilePicture = models.ImageField(upload_to='pics')
    price=models.IntegerField()
    description = models.TextField()

class hotelsss(models.Model):
    name = models.CharField(max_length=30)
    Picture = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    description = models.TextField()
    li1= models.TextField()
    l12=models.TextField()
    l13 = models.TextField()
    l14 = models.TextField()
    l15 = models.TextField()

class categories(models.Model):
    name = models.CharField(max_length=30)
    Picture = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    description = models.TextField()


class  hotel(models.Model):
    destination = models.CharField(max_length=30)
    check_in = models.CharField(max_length=10)
    check_out = models.CharField(max_length=10)
    no_of_rooms = models.IntegerField()
    no_of_adults = models.IntegerField()
    no_of_children = models.IntegerField()
    gender = models.CharField(max_length=20)
    email= models.CharField(max_length=30)
    phone = models.CharField(max_length=10)

class hotels(models.Model):
     destination = models.CharField(max_length=30)
     check_in = models.CharField(max_length=10)
     check_out = models.CharField(max_length=10)
     no_of_rooms = models.IntegerField()
     no_of_adults = models.IntegerField()
     no_of_children = models.IntegerField()
     email = models.CharField(max_length=30)
     phone = models.CharField(max_length=10)

class carss(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    pickup_location= models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    pickup_date= models.CharField(max_length=10)
    hours = models.CharField(max_length=3)
    mins = models.CharField(max_length=3)
    ampm = models.CharField(max_length=10)

class flights(models.Model):
    From = models.CharField(max_length=30)
    to = models.CharField(max_length=30)
    depart = models.CharField(max_length=30)
    Return = models.CharField(max_length=30)
    Class = models.CharField(max_length=30)
    adults= models.IntegerField()
    child = models.IntegerField()

class trainn(models.Model):
    reservation_quota = models.CharField(max_length=30)
    train_name = models.CharField(max_length=30)
    choice_two= models.CharField(max_length=40)
    From= models.CharField(max_length=30)
    to= models.CharField(max_length=30)
    Class= models.CharField(max_length=30)
    date = models.CharField(max_length=10)

class nxt1(models.Model):
    passenger_name= models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=40)
    berth_choice = models.CharField(max_length=30)

class nxt2(models.Model):
    mobile = models.CharField(max_length=10)
    alternative_mobile = models.CharField(max_length=10)
    email= models.CharField(max_length=40)
    account_holdername= models.CharField(max_length=30)
    account_number= models.CharField(max_length=12)
    branch_name= models.CharField(max_length=30)
    wallet = models.CharField(max_length=20)
    phone=models.CharField(max_length=10)


class waterparks(models.Model):
    name_of_destination = models.CharField(max_length=30)
    Picture = models.ImageField(upload_to='pics')
    price=models.IntegerField()
    description = models.TextField()

class viewdetail(models.Model):
    name_of_destination = models.CharField(max_length=100)
    stay = models.CharField(max_length=100)
    desc= models.CharField(max_length=400)
    plan = models.CharField(max_length=300)
    photo= models.ImageField(max_length=120)
    desc1= models.CharField(max_length=300)
    plan2 = models.CharField(max_length=200)
    photo2=models.ImageField(max_length=100)
    desc2 = models.CharField(max_length=100)
    btn = models.CharField(max_length=100)
    btn1 = models.CharField(max_length=100)
    btn2 = models.CharField(max_length=100)
    btn3 = models.CharField(max_length=100)
    btn4 = models.CharField(max_length=100)
    photo3 = models.ImageField(max_length=100)
    photo4 = models.ImageField(max_length=100)
    hotelname = models.CharField(max_length=100)
    pla = models.CharField(max_length=100)
    hotelplan = models.CharField(max_length=100)
    hdes = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

