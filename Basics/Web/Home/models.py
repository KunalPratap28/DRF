from django.db import models

# Create your models here.

class Car(models.Model):
   car_name=models.CharField(max_length=200)
  
   def __str__(self)->str:
     return self.car_name
 
class Person(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    car=models.ForeignKey(Car,null=True,on_delete=models.CASCADE,related_name="car")
    

   