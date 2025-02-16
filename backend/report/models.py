from django.db import models
from patient.models import Patient

# Create your models here.
class Symtom(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Report(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    symtoms = models.ManyToManyField(Symtom)
    
    def __str__(self):
        return f"{self.patient} - {self.location}"