from django.db import models

class Kebele(models.Model):
    name=models.CharField(max_length=100)
    woreda=models.ForeignKey("Woreda",on_delete=models.CASCADE,related_name='kebeles')
class Woreda(models.Model):
    name=models.CharField(max_length=100)
    zone=models.ForeignKey('Zone',on_delete=models.CASCADE,related_name='woredas')
class Zone(models.Model):
    name=models.CharField(max_length=100)
    region=models.ForeignKey('Region',on_delete=models.CASCADE,related_name='zones')
class Region(models.Model):
    name=models.CharField(max_length=100)    
