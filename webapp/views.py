from django.shortcuts import render

#from webapp.models import employees
# Create your views here.
#def home(request):
 #   emp =employees.objects.all()
  #  return render(request,'home.html',{'emp':emp})
#def details(request, pk):
 #  v = employees.objects.get(pk=pk)
  # return render(request, 'details.html', {'v': v})

from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
# def show(request):
#   return HttpResponse('hello world')

# def showpage(request):
#   return render(request,'htmlfile.html')
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

        if pass1 == pass2:
            if User.objects.filter(username=un).exists():
                messages.info(request,'username exists')
            elif User.objects.filter(email=em).exists():
                messages.info(request,'email exists')
            else:
                user = User.objects.create_user(username=un, email=em, password=pass1, first_name=fn, last_name=ln)
                user.save()
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
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
           # return redirect('login')
    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
