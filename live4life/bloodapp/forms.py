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
