from django.db import models
from locations.models import Location

# Create your models here.
class ATM(models.Model):
    name = models.CharField(max_length=200)
    name_vynamic = models.CharField(max_length=100, blank=True, null=True)
    name_way4 = models.CharField(max_length=200, blank=True, null=True)
    terminal_id = models.CharField(max_length=20, blank=True, null=True)
    machine_no = models.CharField(max_length=20, blank=True, null=True)
    gateway = models.CharField(max_length=30, blank=True, null=True)
    ip = models.CharField(max_length=30, blank=True, null=True)
    camera_ip = models.CharField(max_length=30, blank=True, null=True)
    date_setup = models.DateTimeField(null=True, blank=True)
    date_operate = models.DateTimeField(null=True, blank=True)
    date_deactivated = models.DateTimeField(null=True, blank=True)
    ghost_vesion = models.CharField(max_length=30, blank=True, null=True)
    soft_choice = (
        ('ts', 'Terminal Security'),
        ('s', 'Symantec'),
    )
    security_soft = models.CharField(max_length=20, choices=soft_choice, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    status_choice = (
        ('hd', 'Hoạt Động'),
        ('nhd', 'Ngưng Hoạt Động'),
        ('ld', 'Lắp Đặt'),
    )
    status = models.CharField(max_length=20, choices=status_choice, default='hd')

    

    def __str__(self):
        return self.name
    