from django import forms

from .models import Acceptor,Donor


class Acceptorform(forms.ModelForm):
    class Meta:
        model = Acceptor
        fields = ('name', 'group','location','contact','attended')


class Donorform(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ('name', 'group','location','contact','attended')





#class Myform(forms.Form):
    #name = forms.CharField(label='Name', max_length=100)
    #group = forms.MultipleChoiceField( choices=list_of_groups)
    #group = forms.CharField(label='group', max_length=4)
    #location = forms.CharField(label='location' , max_length=150)
    #contact = forms.IntegerField(label = 'contact' , max_value=10)
    