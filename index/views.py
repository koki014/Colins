from typing import List
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.views.generic import (
    ListView
)

from index.models import SalesFeatures, Company, Follow
from product.models import Category
from django.http import HttpResponse, Http404, request, response
from instapi import Client, ClientCompatPatch
from index.tasks import dump_database




class SalesFeaturesListView(ListView):
    model =  SalesFeatures
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company_list'] = Company.objects.all()
        context['category_list'] = Category.objects.all()
        context['link_list'] = Follow.objects.all()
        return context

    
# def category(request):
#     category = Category.objects.all
#     context = {
#         'category_list':category 
#     }  
#     return render(request, 'index.html') 



# def home(request):
#     return render(request, 'index.html')


def dump_database_view(request):
    dump_database.delay()
    return HttpResponse('Database run olundu')


def instagram(requests):
    user_name = '_slymnov_'
    password = '0703331409Nizi'
    api = Client(user_name, password)
    results = api.user_feed('297887086')
    items = results.get('items', [])
    data = Follow.objects.all()
    data.delete()
    for item in items:
        image = item['image_versions2']['candidates'][0]['url']
        title = item['code']
        url = 'https://www.instagram.com/p/'
        
        Follow.objects.create(image=image, title=f'{url}{title}')
        # posts.save()
    
    return redirect(reverse_lazy('home:home'))