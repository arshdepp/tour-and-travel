from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return  render(request,'about.html')
def news(request):
    return render(request,'viewdetails.html')
def contact(request):
    return render(request,'contact.html')