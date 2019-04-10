from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.gis.db import models as gis_models
from django.core.validators import URLValidator

import logging
logger = logging.getLogger(__name__)


class FoodLocation(models.Model):
    """
    Model for FoodLocation
    Campos:
    Descripción:
    Tipo de local:
        - Puesto de comida
        - Local
        - Tianguis (solo algunos días)

    Tipo de comida: (utilizar etiquetas)
        - Tacos
        - Chilaqules
        - tortas
        - Comida corrida
        - etc, etc

    Rango de precios.
    Horarios:
        Hora de apertura y cierre por día de la semana(l,m,m,j,v,s,d).

    Pagina con detalles:
        - link hacia el blog donde se muestran fotos y mas información.

    Dirección.
    Datos de contacto: Facebook, twitter, correo, telefono(s)
    Ubicación:
        - altitud
        - latitud

    Comentarios
    Calificación
    """
    name = models.CharField(
        verbose_name=_('Nombre del negocio'),
        max_length=512,
        default=''
    )

    description = models.TextField(
        verbose_name=_('Descripción'),
        blank=True,
        null=True
    )

    address = models.CharField(
        verbose_name=_('Dirección'),
        max_length=512,
        default=''
    )

    location = gis_models.PointField(
        verbose_name=_('longitud/latitud'),
        geography=True,
        blank=True,
        null=True
    )

    food_type = models.ForeignKey(
        'FoodType',
        on_delete=models.CASCADE,
        verbose_name=_('Tipo de Comida'),
    )

    price_from = models.FloatField(
        verbose_name=_('Precio desde'),
        blank=True,
        default=0
    )

    price_to = models.FloatField(
        verbose_name=_('Precio hasta'),
        blank=True,
        default=0
    )

    rating = models.FloatField(
        verbose_name=_('Calificación'),
        blank=True,
        default=0
    )

    comments = models.TextField(
        verbose_name=_('Comentarios'),
        blank=True,
        null=True
    )

    contact = models.TextField(
        verbose_name=_('Contacto'),
        blank=True,
        null=True
    )

    url_blog = models.TextField(
        validators=[URLValidator()],
        verbose_name=_('Pagina con más info'),
        blank=True,
        null=True
    )

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = _('Lugar de comida')
        verbose_name_plural = _('Lugares de comida')
        ordering = ['name']

    def __str__(self):
        return self.name
