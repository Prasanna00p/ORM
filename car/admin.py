from django.contrib import admin 
from . models import car

admin.site.register(car)

class carAdmin(admin.ModelAdmin): list_display = ('car_id','brand','model','year','price')