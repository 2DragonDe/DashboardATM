from django import forms
from bootstrap_modal_forms.forms import BSModalForm, BSModalModelForm
from fees.models import Summary01

class Summary01Form(BSModalModelForm):

    class Meta:
        model = Summary01
        fields = ('BRANCH', 'ATMNAME', 'TERMINALID', 'PRODUCTNAME', 'SURCHARGEFEE', 'fee_return')
        widgets = {
            'BRANCH': forms.TextInput(attrs={'class': 'form-control', }),
            'ATMNAME': forms.TextInput(attrs={'class': 'form-control', }),
            'TERMINALID': forms.TextInput(attrs={'class': 'form-control', }),
            'PRODUCTNAME': forms.TextInput(attrs={'class': 'form-control', }),
            'SURCHARGEFEE': forms.TextInput(attrs={'class': 'form-control', }),
            'fee_return': forms.TextInput(attrs={'class': 'form-control'}),
        }