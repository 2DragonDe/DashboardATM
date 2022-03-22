from django.urls import path
from atms import views

urlpatterns = [
    path('', views.Index.as_view(), name='atm-home'),
    path('create/',views.ATMCreateView.as_view(), name='atm-create'),
    path('read/<int:pk>', views.ATMReadView.as_view(), name='atm-read'),
    path('update/<int:pk>', views.ATMUpdateView.as_view(), name='atm-update'),
    path('delete/<int:pk>', views.ATMDeleteView.as_view(), name='atm-delete'),
]
