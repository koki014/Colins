from django.urls import path
from product.api.views import (
    
    allProducts, 
    getProduct, 
    createProduct, 
    updateProduct, 
    deleteProduct,
    ProductList
)


app_name = 'product_apis'
urlpatterns = [
    path('products', allProducts, name='products'),
    path('product/<int:pk>/', getProduct, name='product'),
    path('create-product', createProduct, name='create_product'),
    path('update-product/<int:pk>', updateProduct, name='update_product'),
    path('delete-product/<int:pk>/', deleteProduct, name='delete_product'),
    path('<int:pk>/filter_data/', ProductList.as_view(), name='filter_data'),

]