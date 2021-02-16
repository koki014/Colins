from django.urls import path, include
from .views import (
    SalesFeaturesListView,
    dump_database_view,
    instagram
)

app_name = 'home'

urlpatterns = [
    path('', SalesFeaturesListView.as_view(), name='home'),
    path('dump/', dump_database_view, name='dump_database_view'),
    path('api/v1/', include('index.api.urls')),
    path('instagram/',instagram ),
    

]