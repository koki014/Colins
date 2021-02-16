from typing import List
from django.shortcuts import render
from django.views.generic import (
    ListView
)

from meny.models import Meny




class MenyListView(ListView):
    model =  Meny
    context_object_name = 'meny_list'
    template_name = 'index.html'
   