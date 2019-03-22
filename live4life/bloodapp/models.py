from django.db import models
from django.utils import timezone

# Create your models here.
class Acceptor(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)
    group = models.CharField(max_length=3)
    location = models.CharField(max_length=150)
    contact = models.IntegerField()
    attended = models.BooleanField(blank=False,null=False)
    
    def __str__(self):
        return self.name


class Donor(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)
    group = models.CharField(max_length=3)
    location = models.CharField(max_length=150)
    contact = models.IntegerField()
    attended = models.BooleanField(blank=False,null=False)
    
    def __str__(self):
        return self.name