
# Django
from django.urls import path

# Views
from applications.maps.views.lugares import Lugares

urlpatterns = [
    path('lugares/', Lugares.as_view()),
]
