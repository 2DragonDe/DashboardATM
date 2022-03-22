from django.urls import path
from events import views

urlpatterns = [
    path('', views.Index.as_view(), name='event-home'),
    path('create/',views.EventCreateView.as_view(), name='event-create'),
    #path('read/<int:pk>', views.EventsUpdateView.as_view(), name='event-read'),
    path('update/<int:pk>', views.EventUpdateView.as_view(), name='event-update'),
    path('delete/<int:pk>', views.EventDeleteView.as_view(), name='event-delete'),
]
