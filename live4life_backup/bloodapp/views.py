from django.shortcuts import render,redirect

from django.utils import timezone


# Create your views here.
from .models import Acceptor,Donor
from .forms import Acceptorform,Donorform



def index(request):
    return render(request,'index.html')





def dnr_reg(request):
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Donorform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            info = form.save(commit=False)
            info.date_added = timezone.now()
            info.save()

            # ...
            # redirect to a new URL:
            return redirect('/find_dnr/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Acceptorform()

    return render(request, 'donorregistration.html', {'form': form})





def acptr_reg(request):
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Acceptorform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            info = form.save(commit=False)
            info.date_added = timezone.now()
            info.save()


            # ...
            # redirect to a new URL:
            return redirect('/find_acptr/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = Donorform()

    return render(request, 'acceptorregistration.html', {'form': form})







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
