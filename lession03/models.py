from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()

class Car(models.Model):
    idCar = models.AutoField(primary_key=True)
    idManufacturer =models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    color =  models.CharField(max_length=20)

class Manufacturer(models.Model):
    idManufacturer = models.AutoField(primary_key=True)
    nameManufacturer = models.CharField(max_length=100)
    
    
    
