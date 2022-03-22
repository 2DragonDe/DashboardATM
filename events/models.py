from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey

from atms.models import ATM

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class CodeError(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Error(models.Model):    
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    code_error = ChainedForeignKey(
        'CodeError',
        chained_field='department',
        chained_model_field='department',
        show_all=False,
        auto_choose=True,
    )
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class HandlingStaff(models.Model):
    handling_staff = models.CharField(max_length=80)

    def __str__(self):
        return self.handling_staff
    

class Event(models.Model):
    name = models.ForeignKey(ATM, on_delete=models.CASCADE)
    error = models.ForeignKey(Error, on_delete=models.CASCADE)
    status_choice = (
        ('new', 'Mới'),
        ('process', 'Đang Xử Lý'),
        ('complete', 'Hoàn Thành'),
        ('close', 'Kết Thúc'),
    )
    status = models.CharField(max_length=20, choices=status_choice, default='new')
    status_atm_choice = (
        ('in_services', 'In Services'),
        ('out_services', 'Out Of Services'),
        ('offline', 'Offline'),
    )
    status_atm = models.CharField(max_length=20, choices=status_atm_choice, default='out_services')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)
    date_complete = models.DateTimeField(blank=True, null=True)
    date_post = models.DateTimeField(blank=True, null=True)
    date_close = models.DateTimeField(blank=True, null=True)
    priority_choice = (
        ('low', 'Thấp'),
        ('medium', 'Bình Thường'),
        ('high', 'Cao')
    )
    priority = models.CharField(max_length=20, choices=priority_choice, default='medium')
    supervisor_note = models.TextField(blank=True, null=True)
    report24h = models.BooleanField(default=False)
    replace_components = models.BooleanField(default=False)
    end_funds = models.BooleanField(default=False)
    to_funds = models.BooleanField(default=False)
    handling_staff_event = models.ForeignKey(HandlingStaff, on_delete=models.CASCADE,  blank=True, null=True)

    
    def __str__(self):
        return str(self.name)
    
    
    
class Comment(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True)
    event_comment = models.ForeignKey(Event, related_name="comments", on_delete=models.CASCADE )

    def __str__(self):
        return str(self.staff)

    