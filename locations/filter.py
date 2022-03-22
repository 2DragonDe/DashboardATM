from operator import mod
from pyexpat import model
from django import forms
from .models import Location, Manager

from django_select2.forms import Select2Widget
import django_filters

class LocationFilter(django_filters.FilterSet):

    class Meta:
        model = Location
        fields = ('manager', 'fundraiser', 'forcus')
        
    
