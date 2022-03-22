from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Count

from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalDeleteView,
    BSModalFormView,
    BSModalReadView,
    BSModalUpdateView,
)

from locations.forms import LocationForm
from locations.models import Location, City
from .filter import LocationFilter

# Create your views here.
@method_decorator(login_required, name='dispatch')
class Index(generic.ListView):
    model = Location
    context_object_name = 'locations'
    template_name = 'location_home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        locations = Location.objects.all()

        context['total_locations'] = locations.filter(status='hd').count()
        context['total_in'] = locations.filter(area = 'in').count()
        context['total_out'] = locations.filter(area='out').count()
        context['total_forcus'] = locations.filter(forcus=1).count()
        context['filters'] = LocationFilter(self.request.GET, queryset=self.get_queryset())
        return context
    


@method_decorator(login_required, name='dispatch')
class LocationCreateView(BSModalCreateView):
    template_name = 'location_create.html'
    form_class = LocationForm
    success_message = 'Tạo Điểm Lắp Đặt thành công!'
    success_url = reverse_lazy('location-home')

@method_decorator(login_required, name='dispatch')
class LocationReadView(BSModalReadView):
    model = Location
    template_name = 'location_read.html'

@method_decorator(login_required, name='dispatch')
class LocationUpdateView(BSModalUpdateView):
    model = Location
    template_name = 'location_update.html'
    form_class = LocationForm
    success_message = 'Cập nhật thành công!'
    success_url = reverse_lazy('location-home')

@method_decorator(login_required, name='dispatch')
class LocationDeleteView(BSModalDeleteView):
    model = Location
    template_name = 'location_delete.html'
    success_url = reverse_lazy('location-home')
    success_message = 'Đã xoá thành công!'
