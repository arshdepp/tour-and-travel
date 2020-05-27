from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count, Q
from django.core.paginator import Paginator

# Create your views here.
from flyo.models import destinationss, hotels, carss, flights, trainn, nxt1, nxt2, categories, waterparks, hotelsss,viewdetail


def htmlfile(request):
    c = categories.objects.all()
    return render(request, 'htmlfile.html', {'c': c})

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
                messages.info(request, 'username exists')
            elif User.objects.filter(email=em).exists():
                messages.info(request, 'email exists')
            else:
                user = User.objects.create_user(username=un, email=em, password=pass1, first_name=fn, last_name=ln)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password not matched')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        un = request.POST['username']
        pass1 = request.POST['password1']

        user = auth.authenticate(username=un, password=pass1)
        if user is not None:
            auth.login(request, user)
            return redirect('reservations')
        else:
            messages.info(request, 'invalid credentials')
        # return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def aboutt(request):
    return render(request, 'aboutt.html')


def contactus(request):
    return render(request, 'contactus.html')


def servicess(request):
    v = destinationss.objects.all()
    dest1 = destinationss.objects.all()
    search_query = request.GET.get('search')
    if search_query:
        dest1 = dest1.filter(
            Q(name_of_destination__icontains=search_query) |
            Q(price__icontains=search_query)
        )
    paginator = Paginator(dest1, 6)
    page = request.GET.get('page')
    dest1 = paginator.get_page(page)

    return render(request, 'servicess.html', {'v': v, 'dest1': dest1})


def adven(request):
    return render(request, 'adven.html')


def couple(request):
    return render(request, 'couple.html')


def national(request):
    return render(request, 'national.html')


def religious(request):
    return render(request, 'religious.html')


def hotel(request):
    if request.method == 'POST':
        des = request.POST['destination']
        ci = request.POST['checkin']
        cu = request.POST['checkout']
        nor = request.POST['noofrooms']
        noa = request.POST['noofadults']
        noc = request.POST['noofchildren']
        email = request.POST['email']
        phn = request.POST['phon']
        user = hotels(destination=des, check_in=ci, check_out=cu, no_of_adults=noa, no_of_rooms=nor, no_of_children=noc,
                      email=email,
                      phone=phn)
        user.save()
    return render(request, 'hotel.html')


def reservations(request):
    h = hotelsss.objects.all()
    return render(request, 'reservations.html', {'h': h})


def car(request):
    if request.method == 'POST':
        nme = request.POST['name']
        eml = request.POST['email']
        phn = request.POST['phone']
        pul = request.POST['pickuplocation']
        des = request.POST['destination']
        pud = request.POST['pickupdate']
        hrs = request.POST['hours']
        mins = request.POST['mins']
        ap = request.POST['ampm']
        user = carss(name=nme, email=eml, phone=phn, pickup_location=pul, destination=des, pickup_date=pud, hours=hrs,
                   mins=mins, ampm=ap)
        user.save()
    return render(request, 'car.html')


def flight(request):
    if request.method == 'POST':
        Frm = request.POST['From']
        to = request.POST['to']
        dprt = request.POST['depart']
        rtn = request.POST['Return']
        cls = request.POST['Class']
        adlt = request.POST['adults']
        chld = request.POST['child']
        user = flights(From=Frm, to=to, depart=dprt, Return=rtn, Class=cls, adults=adlt,child=chld)
        user.save()
    return render(request, 'flight.html')

def train(request):
    if request.method == 'POST':
        rq = request.POST['reservation_quota']
        tn = request.POST['train_name']
        ct= request.POST['choice_two']
        frm = request.POST['From']
        to = request.POST['to']
        cls = request.POST['Class']
        dt = request.POST['date']
        user = trainn(reservation_quota=rq, train_name=tn, choice_two=ct, From=frm, to=to, Class=cls, date=dt)
        if (rq and frm)and (dt and to) and tn is not None:
            user.save()
            return redirect('next')
        else:
            messages.info(request,'fill data')
    return render(request, 'train.html')
def next(request):
    if request.method == 'POST':
        pn = request.POST['passenger_name']
        age= request.POST['age']
        gndr= request.POST['gender']
        btc = request.POST['berth_choice']

        user = nxt1(passenger_name=pn, age=age, gender=gndr,berth_choice = btc)
        if (pn and age and gndr and btc)is not None:
            user.save()
            return redirect('next2')
        else:
            messages.info(request,'fill data')
    return render(request, 'next.html')
def next2(request):
    if request.method == 'POST':
        mbl = request.POST['mobile']
        almbl = request.POST['alternative_mobile']
        eml = request.POST['email']
        ahn = request.POST['account_holdername']
        an=request.POST['account_number']
        bn = request.POST['branch_name']
        wlt = request.POST['wallet']
        phn = request.POST['phone']
        user = nxt2(mobile=mbl, alternative_mobile=almbl, email=eml, account_holdername=ahn, account_number=an,branch_name=bn,wallet=wlt,phone=phn)
        user.save()
    return render(request, 'next2.html')

def paytm(request):
    return render(request, 'paytm.html')
def water(request):
    w = waterparks.objects.all()
    return render(request, 'water.html',{'w':w})


def home1(request):
    return render(request,'home1.html')

def viewdetails(request):
    vd = viewdetail.objects.all()
    return render(request, 'viewdetails.html',{'vd':vd})