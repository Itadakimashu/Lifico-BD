from django.db import models
from .constants import *

from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    blood_group = models.CharField(max_length=5,choices=blood_groups)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10,choices=genders)
    
    def __str__(self):
        return f'{self.name} - {self.date_of_birth}'