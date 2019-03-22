from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse

from .forms import form1

# Create your views here.
def home(request):
    return render(request,'bloodapp/home.html')

def dnrreg(request):
    #return render(request,'bloodapp/dnrreg.html')
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = form1(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse("thankYou")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = form1()

    return render(request, 'bloodapp/dnrreg.html', {'form': form})

def acptrreg(request):
    #return render(request,'bloodapp/acptrreg.html')
       # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = form1(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse("thankYou")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = form1()

    return render(request, 'bloodapp/acptrreg.html', {'form': form})

