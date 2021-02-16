from django.db import models
from django.utils.translation import gettext as _
from product.models import Category

class Meny(Category):
    # title = models.CharField(_('title'), max_length=50)

    class Meta:
        db_table = _('title')
        verbose_name = _('title')
        verbose_name_plural = _('elave')
        
    def __str__(self):
        return self.title