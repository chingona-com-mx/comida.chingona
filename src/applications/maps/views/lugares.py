
# Django
from django.shortcuts import render
from django.views import View

class Lugares(View):
    def get(self, request):
        return render(request, template_name='maps/map.html')