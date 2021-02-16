from index.api.views import SubscribeView
from django.urls import path



urlpatterns = [
    path('subscribe/', SubscribeView.as_view(), name='subscriber'),
]