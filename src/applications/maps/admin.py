from django.contrib import admin
from applications.maps.models import FoodLocation

class FoodLocationAdmin(admin.ModelAdmin):
    pass
admin.site.register(FoodLocation, FoodLocationAdmin)