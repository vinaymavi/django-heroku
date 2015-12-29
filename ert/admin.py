from django.contrib import admin

# Register your models here.
from .models import Grade,Designation

admin.site.register(Grade)
admin.site.register(Designation)