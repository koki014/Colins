from django.db import models

from django.utils.translation import gettext as _
from django.db import models
from django.db.models.fields.files import ImageField


class Category(models.Model):
    #information
    title = models.CharField(_('novu'), max_length=50, db_index=True)

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = _('category-blog')
        verbose_name = _('kategory')
        verbose_name_plural = _('kategoriler')
        # ordering = ('-icon')

    def __str__(self):
        return self.title


class Slayder(models.Model):
    # information
    image = models.ImageField(_('sekil'),  upload_to='slayder_images')
  
    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = _('slayder-blog')
        verbose_name = _('karusel')
        verbose_name_plural = _('karuseller')
        # ordering = ('-image')

    def __str__(self):
        return str(self.image)


class Blog(models.Model):
    # informations
    title = models.CharField(_('adi'), max_length=100, db_index=True)
    image = models.ImageField(_('sekil'),  upload_to='blog_images', max_length=255,)
    discription = models.TextField(_('aciqlama'))
    face_link = models.CharField('facebook', max_length=255, blank=True, null=True)
    pint_link = models.CharField('pinterest', max_length=255, blank=True, null=True)

    # relations
    category = models.ForeignKey(_('Category'), on_delete=models.CASCADE, related_name="category_id", blank=True, null=True )
    
    # moderations
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = _('blog')
        verbose_name = _('blog')
        verbose_name_plural = _('bloglar')
        # ordering = ('-image')

    def __str__(self):
        return self.title
  

