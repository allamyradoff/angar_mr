from django.contrib import admin
from .models import *

class CarsAdmin(admin.ModelAdmin):
    list_display =  ['name', 'id']


class CarsModelAdmin(admin.ModelAdmin):
    list_display =  ['name', 'car', 'id']

admin.site.register(Dukanlar)
admin.site.register(Zapcas)
admin.site.register(Car, CarsAdmin)
admin.site.register(Car_model, CarsModelAdmin)
admin.site.register(Cars_category)
admin.site.register(Rating)
