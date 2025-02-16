from rest_framework import serializers
from .models import Report, Symtom
from patient.serializers import PatientSerializer

class SymtomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symtom
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    symtoms = SymtomSerializer(many=True,read_only=True)
    patient = PatientSerializer(read_only=True)
    class Meta:
        model = Report
        fields = '__all__'