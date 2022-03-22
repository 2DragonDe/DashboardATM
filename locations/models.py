from operator import mod
from re import T
from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.urls import reverse

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class District(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ward(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Manager(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Fundraiser(models.Model):
    name =  models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class Location(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district = ChainedForeignKey(
        'District',
        chained_field='city',
        chained_model_field='city',
        show_all=False,
        auto_choose=True,
        
    )
    ward = ChainedForeignKey(
        'Ward',
        chained_field='district',
        chained_model_field='district',
        show_all=False,
        auto_choose=True,
        
    )
    street = models.CharField(max_length=200)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    fundraiser = models.ForeignKey(Fundraiser, on_delete=models.CASCADE, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    setup_choice = (
        ('xp', 'XP'),
        ('xt', 'XT'),
        ('s', 'S'),
    )
    setup = models.CharField(max_length=10, choices=setup_choice)
    area_choice = (
        ('in', 'Điểm Trong ACB'),
        ('out', 'Điểm Ngoài ACB'),
    )
    forcus = models.BooleanField(default=False, blank=True, null=True)
    area = models.CharField(max_length=20, choices=area_choice)
    contact01 = models.CharField(max_length=100, blank=True, null=True)
    contact02 = models.CharField(max_length=100, blank=True, null=True)
    contact03 = models.CharField(max_length=100, blank=True, null=True)
    contact04 = models.CharField(max_length=100, blank=True, null=True)
    status_choice = (
        ('nhd', 'Ngưng Hoạt Động'),
        ('hd', 'Hoạt Động'),
    )
    status = models.CharField(max_length=20, choices=status_choice, default='hd', blank=True
    , null=True)

    def __str__(self):
        return self.name

    

    
    
    
    