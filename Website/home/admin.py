from django.contrib import admin
from .models import Department,Docters,Booking

# Register your models here.
admin.site.register(Department)
admin.site.register(Docters)
admin.site.register(Booking)