from django.db import models
from django.utils import timezone

# Create your models here.
class Acceptor(models.Model):
    name = models.CharField(max_length=50)
    group = models.CharField(max_length=10)
    date_added = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=100)
    contact = models.IntegerField()

class Donor(models.Model):
    name = models.CharField(max_length=50)
    group = models.CharField(max_length=10)
    date_added = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=100)
    contact = models.IntegerField()