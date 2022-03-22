from django import forms
from bootstrap_modal_forms.forms import BSModalForm, BSModalModelForm
from atms.models import ATM

class ATMForm(BSModalModelForm):

    class Meta:
        model = ATM
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tên ATM/CDM'}),
            'name_vynamic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tên Vynamic View'}),
            'name_way4': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tên WAY4'}),
            'terminal_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Terminal ID'}),
            'machine_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Machine NO'}),
            'gateway': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Gateway'}),
            'ip': forms.TextInput(attrs={'class': 'form-control','placeholder': 'IP ATM'}),
            'camera_ip': forms.TextInput(attrs={'class': 'form-control','placeholder': 'IP Camera'}),
            'date_setup': forms.DateTimeInput(format='%m/%d/%Y', attrs={'class': 'form-control datepicker','placeholder': 'Ngày Lắp Đặt'}),
            'date_operate': forms.DateTimeInput(format='%m/%d/%Y', attrs={'class':'form-control datepicker', 'placeholder': 'Ngày Vận Hành'}),
            'date_deactivated': forms.DateTimeInput(format='%m/%d/%Y', attrs={'class':'form-control datepicker', 'placeholder': 'Ngày Ngưng Hoạt Động'}),
            'ghost_vesion': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Phiên Bản Ghost'}),
            'security_soft': forms.Select(attrs={'class': 'form-control selectpicker', 'data-style': 'btn btn-rose btn-sm', 'placeholder': 'Phần Mềm Bảo Mật'}),
            'status': forms.Select(attrs={'class': 'form-control selectpicker', 'data-style': 'btn btn-rose btn-sm', 'placeholder': 'Trạng Thái'}),
            

        }

