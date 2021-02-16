from django.db import models
from django.utils.translation import gettext as _

class SalesFeatures(models.Model):
    #information
    image = models.ImageField(_('sekil'),  upload_to='icon_images')
    white_text = models.CharField(_('white'), max_length=50)
    red_text = models.CharField(_('red'), max_length=50)



    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = _('sales')
        verbose_name = _('Satis')
        verbose_name_plural = _('Satis ozellikleri')
        # ordering = ('-icon')

    def __str__(self):
        return self.white_text


class Slayder(models.Model):
    # information
    CATEGORY_CHOICES = (
        ('pro', _('product')),
        ('catgry', _('category')),
        
    )
    image = models.ImageField(_('sekil'),  upload_to='slayder_images')
    sorgu = models.PositiveIntegerField(_("sorgu: "), choices=CATEGORY_CHOICES)

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = _('slayder')
        verbose_name = _('karusel')
        verbose_name_plural = _('karuseller')
        # ordering = ('-image')

    def __str__(self):
        return self.image


class Discovery(models.Model):
    #information
    CATEGORY_CHOICES = (
        ('pro', _('product')),
        ('catgry', _('category')),
        
    )
    image = models.ImageField(_('sekil'),  upload_to='discovery_images')
    sorgu = models.PositiveIntegerField(_("sorgu: "), choices=CATEGORY_CHOICES)

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = _('discovery')
        verbose_name = _('kesf')
        verbose_name_plural = _('kesf et')
        # ordering = ('-image')

    def __str__(self):
        return self.title



class Follow(models.Model):
    #information
    title = models.CharField('link', max_length=400)
    image = models.CharField('sekil', max_length=400)

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'follow'
        verbose_name = 'takib'
        verbose_name_plural = 'takibler'
        # ordering = ('-image')

    def __str__(self):
        return self.title    


class Company(models.Model):
    #information
    CATEGORY_CHOICES = (
        ('pro', _('product')),
        ('catgry', _('category')),
        
    )
    image = models.ImageField(_('sekil'),  upload_to='company_images')
    sorgu = models.CharField(_("sorgu: "), max_length=30, choices=CATEGORY_CHOICES)

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = _('company')
        verbose_name = _('kanpanya')
        verbose_name_plural = _('kanpanyalar')
        # ordering = ('-image')

    def __str__(self):
        return self.sorgu


class Subscriber(models.Model):
    email = models.EmailField(_('email address'), unique=True,)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Subscriber')
        verbose_name_plural = _('Subscribers')

    def __str__(self):
        return self.email

    


