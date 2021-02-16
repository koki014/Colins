from django import forms
from .models import Subscriber


class SendEmailForm(forms.Form):
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={
        'class': 'form-control', 
        'placeholder': 'E-mail'
    }), )

    class Meta:
        model = Subscriber
        fields = (
            'email',
        )
