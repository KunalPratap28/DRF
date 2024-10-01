from rest_framework import serializers
from . import models

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Car
        fields=['car_name']
        
class PersonSerializer(serializers.ModelSerializer):
    car=CarSerializer()
    class Meta:
        model=models.Person
        fields='__all__'
        
    def validate(self,data):
        if data['age']<18:
            raise serializers.ValidationError('Age should be greater than 18') 
        return data