from select import select
from django import forms
from bootstrap_modal_forms.forms import BSModalForm, BSModalModelForm
from django_select2.forms import Select2Widget
from locations.models import Location

class LocationForm(BSModalModelForm):
    
          
    class Meta:
        model = Location
        exclude = ('setup',)
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
            'setup': Select2Widget,
            'area': Select2Widget,
            'forcus': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'contact01': forms.TextInput(attrs={'class': 'form-control'}),
            'contact02': forms.TextInput(attrs={'class': 'form-control'}),
            'contact03': forms.TextInput(attrs={'class': 'form-control'}),
            'contact04': forms.TextInput(attrs={'class': 'form-control'}),
            'status': Select2Widget,
            'manager': Select2Widget,
            #'city': Select2Widget,
            #'district': Select2Widget,
            #'ward': Select2Widget,
            'fundraiser': Select2Widget,
            
        }
        
       
    
    