from django.contrib import admin
from applications.maps.models import FoodLocation


class FoodLocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating']
    ordering = ['-rating']
    # fieldsets = [
    #    ("Información general", {
    #     'fields': ['name',
    #                'description',
    #                'contact',
    #                ]
    #     }),
    #    ("Detalles", {
    #        'fields': [
    #            'food_type',
    #            'rating',
    #            'price_from',
    #            'price_to',
    #            'comments',
    #            'url_blog',
    #        ]
    #    }),
    #    ('Ubicación', {
    #     'fields': [
    #         'address',
    #     ]
    #     }),
    #]
admin.site.register(FoodLocation, FoodLocationAdmin)
