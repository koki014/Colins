from re import T
from django.db import models
from django.db.models.fields import EmailField
from django.contrib.auth.models import AbstractUser, UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    username_validator = UnicodeUsernameValidator
    username = models.CharField(
        _('username'),
        max_length=150,
        blank=True,
        null=True,
        unique=False,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    GENDER_CHOICE = [
        ('M',_('Male')),
        ('F',_('Female')),]
    email = models.EmailField(_('email address'), unique=True,)

    # information
    tel_numb = models.CharField(_('number'), max_length=20)
    birthday_data = models.CharField(_('data'), max_length=50, blank=True, null=True)
    gender = models.CharField(_('gender :'), max_length=30, choices=GENDER_CHOICE,blank=True, null=True)
    is_information = models.BooleanField(_('Tanıtım ve bilgilendirme amacıyla gönderilecek SMS ve E-posta iletilerini kabul ediyorum.'), blank=True, null=True)
    is_membership = models.BooleanField(_('Üyelik sözleşmesini okudum ve kabul ediyorum'), blank=True, null=True)
    
    
    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email 



    
    

   


