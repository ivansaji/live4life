from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'bloodapp/home.html')

def dnrreg(request):
    return render(request,'bloodapp/dnrreg.html')

def acptrreg(request):
    return render(request,'bloodapp/acptrreg.html')