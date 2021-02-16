from django.shortcuts import render
from .models import Category, Product, ProductImg
from meny.models import Meny
from django.template.loader import render_to_string
from django.http import JsonResponse

def product(request, pk):
    product = Product.objects.get(pk=pk)
    # image = ProductImg.objects.all()
    context = {
        'product':product,
        # 'image_list': image
    }
    return render(request, 'product.html', context)


def products(request):
    products = Product.objects.all()
    meny = Meny.objects.all()
    image = ProductImg.objects.all()
    context = {
        'product_list': products,

    }
    return render(request, 'products.html', context)


def product_filter(request, pk):
    category = Category.objects.get(pk=pk)
   
    products = Product.objects.filter(category =  category)
    sort = request.GET.get('sort')
    
    if sort:
        if sort == 'decrease':
            products = products.order_by('-price')
        elif sort == 'increase':
            products = products.order_by('price')
        elif sort == 'a-to-z':
            products = products.order_by('-title') 
        elif sort == 'z-to-a':
            products = products.order_by('title')
    # elif category.is_main:
    #     all_categories = category.category.all()
    #     for categories in all_categories:
    #         print(categories)
    #     products = Product.objects.filter()
    # else:
    #     products = Product.objects.filter(category = category)
    context = {
        'product_list': products,
        'category':category,
       

    }
    return render(request, 'products.html', context)
    

