from __future__ import unicode_literals
from django.db import models

# Create your models here.
class  employees(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    age=models.IntegerField()
    salary=models.IntegerField()
    profilePicture = models.ImageField(upload_to= 'pics')


class videos(models.Model):
    title=models.CharField(max_length=15)
    description=models.TextField()
    album=models.CharField(max_length=20)
    extra=models.CharField(max_length=20)
    offer=models.BooleanField(default=False)
    cont=models.ImageField(upload_to='pics')
    videofile= models.FileField(upload_to='videos',null=True,verbose_name="video_file")