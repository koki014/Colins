from django.db import models
from django.utils.translation import gettext as _


class Contact(models.Model):
    #information
    SUBJECT_CHOICES = (
        ('konu', _('Konu')),
        ('inf', _('Bilgi')),
        ('oner', _('Oneri')),
        ('shik', _('Sikayet')),
        ('talep', _('Talep')),
        ('tsk', _('Tesekkur')),
    )
    SUb_SUBJECT_CHOICES = (
        ('alt konu'), _('Alt Konu')),
    
    subject = models.CharField(_('subject'),max_length=255, choices=SUBJECT_CHOICES)
    name = models.CharField(_('name'), max_length=50)
    email = models.EmailField(_('email'),max_length=50)
    tel_number = models.CharField(_('telefon'), max_length=20)
    sub_subject = models.CharField(_('subject'),max_length=255, choices=SUb_SUBJECT_CHOICES)
    message = models.TextField(_('message'))


    # moderations
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = _('contact')
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')
        
    def __str__(self):
        return self.name
