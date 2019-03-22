from django.shortcuts import render

# Create your views here.
from .models import Acceptor,Donor



def index(request):
    return render(request,'index.html')

def dnr_reg(request):
    #dnr reg code
    
    return render(request,'donorregistration.html')

def acptr_reg(request):
    #acptr_reg code

    return render(request,'acceptorregistration.html')

def find_dnr(request):
    #find donor code
    donor_list = Donor.objects.order_by('-date_added')
    
    context = {'donor_list' : donor_list}

    return render(request,'finddonor.html',context)

def find_acptr(request):
    #find acceptor code
    acptr_list = Acceptor.objects.order_by('-date_added')
    
    context = {'acptr_list' : acptr_list}

    return render(request,'findacceptor.html',context)