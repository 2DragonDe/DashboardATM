from django.contrib import admin
from .models import Department, CodeError, Error, Event, Comment, HandlingStaff

# Register your models here.
admin.site.register(Department)
admin.site.register(CodeError)
admin.site.register(Error)
admin.site.register(Event)
admin.site.register(Comment)
admin.site.register(HandlingStaff)