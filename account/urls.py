from django.urls import path, re_path, include
from django.contrib.auth.views import LogoutView
from .views import (
    RegisterView, 
    CustomLoginView,
    UserActivate,
    CustomPasswordChangeView,
    CustomPasswordResetView,
    CustomPasswordResetConfirmView,
    PasswordResetCompletedView,
    CustomPasswordResetDoneView,
    UpdateStoryView
    
)


app_name = 'account'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',
        UserActivate.as_view(), name='activate'),
    path('changepassword/', CustomPasswordChangeView.as_view(), name='change_password'),
    path('passwordrecovery/', CustomPasswordResetView.as_view(), name='reset_password'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-completed/', PasswordResetCompletedView.as_view(), name='password_reset_completed'),
    path('reset-done/', CustomPasswordResetDoneView.as_view(), name='reset_done'),
    path('update-info/<int:pk>/', UpdateStoryView.as_view(), name='update_info'),
    path('api/v1/', include('account.api.urls'))
]