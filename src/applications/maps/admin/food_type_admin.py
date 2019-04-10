from django.contrib import admin
from applications.maps.models import FoodType


class FoodTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(FoodType, FoodTypeAdmin)
