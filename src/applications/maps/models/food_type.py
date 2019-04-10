from django.db import models
from django.utils.translation import ugettext_lazy as _

import logging
logger = logging.getLogger(__name__)


class FoodType(models.Model):
    """
    Tipo de comida: (utilizar etiquetas)
        - Tacos
        - Chilaqules
        - tortas
        - Comida corrida
        - etc, etc

    """
    name = models.CharField(
        verbose_name=_('Tipo de comida'),
        max_length=200,
        default=''
    )

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = _('Tipo de comida')
        verbose_name_plural = _('Tipos de comida')
        ordering = ['name']

    def __str__(self):
        return self.name
