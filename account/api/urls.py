from account.api.views import CustomAuthToken, UserRegisterAPIView
from django.urls import path

urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='auth_login'),
    path('register/', UserRegisterAPIView.as_view(), name='auth_register'),
]