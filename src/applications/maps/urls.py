
# Django
from django.urls import path, include

# Views
from applications.maps.views.lugares import Lugares, LugaresViewSet

# Rest frameworkd
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'lugares', LugaresViewSet)


urlpatterns = [
    path('', Lugares.as_view()),
    path('', include(router.urls)),
]
