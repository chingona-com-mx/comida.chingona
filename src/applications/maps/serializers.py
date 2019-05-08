
# Rest framework
from rest_framework_gis.serializers import GeoFeatureModelSerializer

# Models
from applications.maps.models import FoodLocation


class FoodLocationSerializer(GeoFeatureModelSerializer):
    """Serializer para agregar/mostrar lugares de comida"""
    class Meta:
        model = FoodLocation
        geo_field = 'location'
        fields = (
            'id',
            'name',
            'description',
            'address',
            'food_type',
            'price_from',
            'price_to',
            'rating',
            'comments',
            'contact',
            'url_blog',
            'created',
            'updated',
        )
