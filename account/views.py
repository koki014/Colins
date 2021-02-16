from django.shortcuts import render, redirect
from account.forms import (
    CustomUserForm, 
    LoginForm, 
    CustomPasswordChangeForm, 
    CustomPasswordResetForm,
    CustomSetPasswordForm,
)
from django.contrib.messages import success
from account.tasks import send_confirmation_email
from django.views.generic import CreateView, View, UpdateView
from django.urls.base import reverse_lazy
from django.contrib.auth import get_user_model
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import authenticate, login as django_login
from account.tools.tokens import account_activation_token
from django.contrib.auth.views import (
     LoginView,
     PasswordChangeView,
     PasswordResetView,
     PasswordResetConfirmView,
     PasswordResetDoneView,
     PasswordResetCompleteView,
     
)


User = get_user_model()
# def register(request):
#     form = CustomUserForm()
#     if request.method == 'POST':
#         form = CustomUserForm(data=request.POST)
#         print(request.POST, 'invalid')
#         if form.is_valid():
#             print(form, 'sasaaasa')
#             user = form.save()
#             user.is_active = False
#             user.save()
#             # site_address = request.is_secure() and "https://" or "http://" + request.META['HTTP_HOST']  # https://stackoverflow.com/
#             # send_confirmation_email(user, site_address)
#             return redirect(reverse_lazy('account:login'))
            
#     context = {
#         'form':form
#     }
#     return render(request, 'register.html', context)



class RegisterView(CreateView):
    form_class = CustomUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('account:login')
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        site_address = self.request.is_secure() and "https://" or "http://" + self.request.META['HTTP_HOST']  # https
        # ://stackoverflow.com/
        send_confirmation_email(user, site_address)
        return super().form_valid(form)


class UserActivate(View):
    def get(self, request, *args, **kwargs):
        uidb64 = kwargs.get('uidb64')
        token = kwargs.get('token')
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect(reverse_lazy('account:login'))
            

        

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'


class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'change_password.html'
    success_url = reverse_lazy('account:change_password')
    def form_valid(self, form):
        success(self.request, 'Şifreniz başarıyla değiştirilmiştir.')
        return super().form_valid(form)


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'forget_password.html'
    email_template_name = 'email/password_reset_email.html'
    success_url = reverse_lazy('account:password_reset_completed')



class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'reset_password.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('account:reset_done')


class PasswordResetCompletedView(PasswordResetCompleteView):
    template_name = 'password_reset_completed.html'


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'reset_done.html'


class UpdateStoryView(UpdateView):
    model = User
    form_class = CustomUserForm
    template_name = 'account_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['in_update_view'] = True
        return context
