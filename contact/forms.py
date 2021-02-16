from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    subject = forms.ChoiceField(widget = forms.Select(attrs={
                'class': 'form-control col-12',
                
            }) , 
                     choices = (
        [('konu', 'Konu'),
        ('inf', 'Bilgi'),
        ('oner', 'Oneri'),
        ('shik', 'Sikayet'),
        ('talep', 'Talep'),
        ('tsk', 'Tesekkur')]
    ), initial='konu', required = True,)
    sub_subject = forms.ChoiceField(widget = forms.Select(attrs={
                'class': 'form-control col-12',
                
            }) , 
                     choices = (
        [('alt konu', 'Alt Konu'),
        ]
    ), initial='alt konu', required = True,)
    class Meta:
        model = Contact
        fields = (
            'subject',
            'sub_subject',
            'name',
            'email',
            'tel_number',
            'message',
            
        )

        widgets = {
            
            'name': forms.TextInput(attrs={
                'class': 'form-control col-12',
                'placeholder': 'Ad '
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control ',
                'placeholder': 'E-posta adresiniz'
            }),
            'tel_number': forms.NumberInput(attrs={
                'class': 'form-control ',
                'placeholder': 'Telefon'
            }),
            
            'message': forms.Textarea(attrs={
                'class': 'form-control col-12',
                'placeholder': 'Mesaj'
            }),
            

        }