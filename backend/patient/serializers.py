from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', write_only=True)
    password = serializers.CharField(source='user.password', write_only=True)
    class Meta:
        model = Patient
        fields = ('id','name', 'gender', 'phone', 'blood_group','date_of_birth','username','password')
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(username=user_data['username'], password=user_data['password'])
        patient = Patient.objects.create(user=user, **validated_data)
        return patient