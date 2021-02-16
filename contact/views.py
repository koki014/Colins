from django.shortcuts import render
from django.views.generic import CreateView
from django.urls.base import reverse_lazy
from .forms import ContactForm


class ContactCreateView(CreateView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('home:home')
