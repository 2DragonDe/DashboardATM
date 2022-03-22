from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q

from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalDeleteView,
    BSModalFormView,
    BSModalReadView,
    BSModalUpdateView,
)

from atms.models import ATM
from locations.models import Location
from atms.forms import ATMForm

# Create your views here.
@method_decorator(login_required, name='dispatch')
class Index(generic.ListView):
    model = ATM
    context_object_name = 'atms'
    template_name = 'atm_home.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        atms = ATM.objects.all()

        context['total_atms'] = atms.filter(status='hd').count()
        context['total_atm'] = atms.filter(name__contains='atm').count()
        context['total_cdm'] = atms.filter(name__contains='cdm').count()
        return context
    
@method_decorator(login_required, name='dispatch')
class ATMCreateView(BSModalCreateView):
    template_name = 'atm_create.html'
    form_class = ATMForm
    success_message = 'Thành công: Một ATM mới đã được khởi tạo!'
    success_url = reverse_lazy('atm-home')

@method_decorator(login_required, name='dispatch')
class ATMReadView(BSModalReadView):
    model = ATM
    template_name = 'atm_read.html'

@method_decorator(login_required, name='dispatch')
class ATMUpdateView(BSModalUpdateView) :
    model = ATM
    form_class = ATMForm
    template_name = 'atm_update.html'
    success_message = 'Thành công: ATM đã được cập nhật!'
    success_url = reverse_lazy('atm-home')

@method_decorator(login_required, name='dispatch')
class ATMDeleteView(BSModalDeleteView):
    model = ATM
    template_name = 'atm_delete.html'
    success_message = 'Thành công: ATM đã được xóa hoàn toàn!'
    success_url = reverse_lazy('atm-home')