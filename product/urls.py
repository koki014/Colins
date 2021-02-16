from django.urls import path, include
from .views import product, products, product_filter
from django.conf import settings
from django.conf.urls.static import static

app_name='product'

urlpatterns = [
    path('<int:pk>/', product, name='product'),
    path('', products, name='products'),
    path('filter/<int:pk>/', product_filter, name='filter_products'),

] 
