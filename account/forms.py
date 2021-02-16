from django import forms
from django.contrib.auth.forms import (
    UserCreationForm ,
    AuthenticationForm, 
    UsernameField, 
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
    
)
from django.contrib.auth import get_user_model
from django.db.models.fields import EmailField
from django.forms import SelectDateWidget
import datetime
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class CustomUserForm(UserCreationForm):
    gender= forms.ChoiceField(widget = forms.RadioSelect(attrs={
                'class': 'checkmark',
                  
                
            }) , 
                     choices = (
        [('M','Erkek'),
        ('F','Kadin'),]
    ), required = True,)

    password1 = forms.CharField(required=True, widget = forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Password'
        }), label = 'Password') 

    birthday_data = forms.DateField(widget= SelectDateWidget(attrs={'class':'form-control datecustom '}, years=range(1951, datetime.datetime.now().year + 1)))
    class Meta:
        model = User
        fields = (
            'gender',
            'password1',
            'birthday_data',
            'email',
            'first_name',
            'last_name',
            'tel_numb',
            'is_information',
            'is_membership',    
            
            
        )
        widgets = {
             'email': forms.EmailInput(attrs={
                'class': 'form-control ',
                'placeholder': 'E-posta adresiniz'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control ',
                'placeholder': 'Ad '
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Soyad'
            }),
            'tel_numb': forms.TextInput(attrs={
                'class': 'form-control ',
                'placeholder': 'Telefon numaraniz'
            }),
            'is_information': forms.CheckboxInput(attrs={
                'class': 'custom-control-input',
                'name': "SMSSubscribe",
                'id': "SMSSubscribe"
            }),
            'is_membership': forms.CheckboxInput(attrs={
                'class': 'custom-control-input',
                'name': 'AcceptRegistrationRules',
                'id': 'AcceptRegistrationRules',
                
            }),


        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']
        



class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control',}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
        })
    )


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus': True, 'class': 'form-control','placeholder' : 'Eski şifre', 'id':'showOldPassword' }),
    )
    new_password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder' : 'Yeni şifre', 'id':'showNewPassword'}),
    )
    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder' : 'Yeni şifre (Tekrar)'}),
    )


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={
        'class': 'form-control', 
        'placeholder': 'E-posta adresi'
    }), )


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder' : 'Şifre'
        }),
    )
    new_password2 = forms.CharField(

        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder' : 'Yeni şifre'
        }),
    )