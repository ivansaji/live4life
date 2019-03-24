from django.contrib import admin

# Register your models here.

from .models import Acceptor,Donor

admin.site.register(Acceptor)
admin.site.register(Donor)