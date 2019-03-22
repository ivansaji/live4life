from django import forms
from django.utils import timezone

from .models import Acceptor,Donor

bloodgroup=('A +ve','A -ve','B +ve','B -ve',)

class form1(forms.Form):
    name = forms.CharField(label='name',max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name','id':'name',}))
    group = forms.CharField(label='name',max_length=3,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Blood Group(A+,B+,AB+ etc)','id':'group',}))
    #group = forms.ChoiceField(choices=bloodgroup,label='group',widget=forms.Select)
    location = forms.CharField(label='location',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Location','id':'location',}))
    contact = forms.IntegerField(label='contact',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Contact Number','id':'location','type':'number',}))

