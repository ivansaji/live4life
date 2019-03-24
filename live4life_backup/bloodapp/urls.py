"""live4life URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name='bloodapp'
urlpatterns = [
    path('' , views.index , name='index'),
    path('dnr-reg/' , views.dnr_reg , name='donorreg'),
    path('acptr-reg/' , views.acptr_reg , name='acceptorreg'),
    path('find_dnr/',views.find_dnr , name='finddonor'),
    path('find_acptr/',views.find_acptr , name='findacceptor'),
    
]
