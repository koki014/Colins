from django.urls import path
from .views import (
    MenyListView
)

app_name = 'home'

urlpatterns = [
    path('', MenyListView.as_view(), name='home'),

]