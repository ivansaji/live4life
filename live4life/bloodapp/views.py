from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'bloodapp/home.html')

def donorreg(request):
    return render(request,'bloodapp/home.html')

def acceptreg(request):
    return render(request,'bloodapp/home.html')