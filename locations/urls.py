from django.urls import path
from locations import views

urlpatterns = [
    path('', views.Index.as_view(), name='location-home'),
    path('create/',views.LocationCreateView.as_view(), name='location-create'),
    path('read/<int:pk>', views.LocationReadView.as_view(), name='location-read'),
    path('update/<int:pk>', views.LocationUpdateView.as_view(), name='location-update'),
    path('delete/<int:pk>', views.LocationDeleteView.as_view(), name='location-delete'),
]
