from __future__ import unicode_literals
from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic.base import View
from flyo.models import data
from flyo.token import account_activation_token

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import  get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import data
from .serializers import dataSerializer
from rest_framework import viewsets

# Create your views here.
class employeeList(APIView):
    def get(self,request):
        employee1=data.objects.all()
        serializer=dataSerializer(employee1,many=True)
        return Response(serializer.data)

    #def post(self):
     #   pass
class employeeListPost(APIView):
    def post(self, request):
        serializer = dataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#class EmployeeViewSet(viewsets.ModelViewSet):
def api_veiw(param):
    pass


#@api_veiw(['GET','PUT','DELETE'])
#def details(request , pk):
 #try:
  #   data1 = data.objects.get(pk=pk)
 #except data.DoesNotExist:
  #   return Response(status=status.HTTP_404_NOT_FOUND)

 #if request.method =='GET':
  #      serializer = dataSerializer(data1)
   #     return Response(serializer.data)
 #elif request.method == 'PUT':
  #     serializer = dataSerializer(data1,data=request.data)
   #    if serializer.is_valid():
    #      serializer.save()
     #     return Response(serializer.data)
      # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

 #elif request.method == 'DELETE':
  #   data1.delete()
   #  return Response(status=status.HTTP_204_NO_CONTENT)


def home(request):
    return render(request, 'home.html')
def register(request):
    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        un = request.POST['username']
        em = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        gd = request.POST['gender']
        dob = request.POST['Date_Of_Birth']
        mn = request.POST['mobile_number']
        if pass1 == pass2:
                user = data(username=un, email=em, password=pass1, first_name=fn, last_name=ln,gender=gd,birth=dob,mobile_number=mn)
                data1 =User.objects.create_user(username=un, email=em, password=pass1)
                data1.save()
                user.is_active = False
                user.save()

                current_site = get_current_site(request)

                subject = 'Activate your Account'

                message = render_to_string('activate_account.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })

                send_mail(
                    subject,
                    message,
                    EMAIL_HOST_USER,
                    [em],
                    fail_silently=False,
                )
                return redirect('login')
        else:
            messages.info(request,'password not matched')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        un = request.POST['username']
        pass1 = request.POST['password1']

        user = auth.authenticate(username=un, password=pass1)
        if user is not None:
            auth.login(request, user)
            return redirect('htmlfile')
        else:
            messages.info(request,'invalid credentials')
           # return redirect('login')
    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('login')


class ActivateAccount(View):
    def get(self,request,uidb64,token, *args, **kwargs):
        try:
            #uid =force_text(urlsafe_base64_decode(uidb64)
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user=None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active =True
            user.save()
            login(request)
            messages.success(request, ('Your Account have been confirmed.'))
            print("Confirmed",user.is_active)
            return render(request,'htmlfile.html')
        else:
            messages.warning(request, ('The confirmation link was invalid'))
            return redirect('/')



def home1(request):
    return render(request,'home1.html')


def details(request):
    return render(request,'details.html')
