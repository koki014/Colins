from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import related
from django.db.models.fields.files import ImageField
from django.utils.translation import gettext as _


class Category(models.Model):
    IS_CHOICES = (
        ('up', _('up')),
        ('down', _('down')),
        ('m', _('middle')),
        ('no', _('none'))
        
        
    )

    # information
    title = models.CharField(_('title'), max_length=50, db_index=True)
    image = models.ImageField(_('Image: '), upload_to='caregory_images', blank=True, null=True)
    is_active_class = models.BooleanField(_('yasil reng'), default=False)
    is_main = models.BooleanField(_('esas'), default=False)
    is_sub = models.BooleanField(_('orta'), default=False)
    slug = models.SlugField(_('slug'), blank=True, null=True, editable=False, unique=True)
    is_position = models.CharField('is position', max_length=50, choices=IS_CHOICES)

    
    #relations
    parent_category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category', blank=True, null=True)
    related_category = models.ManyToManyField('Category', related_name = 'related_categories', blank=True)
    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = _('category')
        verbose_name = _('kategoriya')
        verbose_name_plural = _('kategoriyalar')
        
    def __str__(self):
        if self.is_main:
            s = f'{self.title} is_main'
        elif self.is_sub:
            s = f'{self.title} is_sub'
        else:
            s = f'{self.title} {self.parent_category} {self.slug}'
        return s 


class Product(models.Model):
    CATEGORY_CHOICES = (
        ('xs', 'XS'),
        ('s', 'S'),
        ('m', 'M'),
        ('l', 'L'),
        ('xl', 'XL'),
        ('xxl', 'XXL'),
        
    )

    # information
    title = models.CharField(_('title'), max_length=100, db_index=True)
    price = models.FloatField(_('price') )
    image = models.ImageField(_("Image: "), upload_to='product_image')
    size = models.CharField(_("size: "),max_length=20, choices=CATEGORY_CHOICES)
    color_name = models.CharField(_('color'), max_length=20)
    code = models.CharField(_('urun kodu'), max_length=30)
    content = models.CharField(_('urun iceriyi'), max_length=30)
    fit = models.CharField(_('fit'), max_length=30)
    sezon = models.CharField(_('sezon'), max_length=30)
    slug = models.SlugField(_('slug'), blank=True, null=True)
        
    #relations
    category = models.ManyToManyField('Category', related_name='category_id', blank=True)
    color = models.ManyToManyField('Product', related_name='color_id', blank=True)
    


    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        db_table = _('product')
        verbose_name = _('mehsul')
        verbose_name_plural = _('mehsullar')
        
    def __str__(self):
        return self.title 







class ProductImg(models.Model):
    #information
    is_main = models.BooleanField(_('esas'), default=True)
    image = models.ImageField(_('Image'), upload_to='product_images')
    

    #relations
    pro_rel = models.ForeignKey ('Product', on_delete=models.CASCADE, related_name='rel_id')


    #moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = _('image')
        verbose_name = _('sekil')
        verbose_name_plural = _('sekiller')
        
    def __str__(self):
        return self.pro_rel.title