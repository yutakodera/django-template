from datetime import timedelta
import os

from django.conf import settings
from django.utils import timezone
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import (
     get_user_model, logout as auth_logout,
)
from django.http import HttpResponse
from django.core.mail import send_mail

from .forms import UserCreateForm, ResendActivationEmailForm
from .models import UserActivateTokens



User = get_user_model()

class Top(generic.TemplateView):
    template_name = 'top.html'

class BeforeActivation(generic.TemplateView):
    template_name = 'registration/before_activation.html'

class SignUpView(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('accounts:before-activation')
    template_name = 'registration/signup.html'


class ProfileView(LoginRequiredMixin, generic.View):

    def get(self, *args, **kwargs):
        return render(self.request,'registration/profile.html')


class DeleteView(LoginRequiredMixin, generic.View):

    def get(self, *args, **kwargs):
        user = User.objects.get(email=self.request.user.email)
        user.is_active = False
        user.save()
        auth_logout(self.request)
        return render(self.request,'registration/delete_complete.html')

def activate_user(request, activate_token):
    activated_user = UserActivateTokens.objects.activate_user_by_token(
        activate_token)
    if hasattr(activated_user, 'is_active'):
        if activated_user.is_active:
            message = 'ユーザーのアクティベーションが完了しました'
        if not activated_user.is_active:
            message = 'アクティベーションが失敗しています。管理者に問い合わせてください'
    if not hasattr(activated_user, 'is_active'):
        message = 'エラーが発生しました'
    return HttpResponse(message)

def resend_activation_email(request):

    form = ResendActivationEmailForm()
    message = ''
    if request.method == 'POST':
        form = ResendActivationEmailForm(request.POST)
        if form.is_valid():
            if User.objects.filter(email=form.cleaned_data['email']).exists():
                user = User.objects.get(email=form.cleaned_data['email'])
            else:
                message = 'メールアドレスが存在しません。'
                return render(request, 'registration/resend_activation_email.html', {'form': form, 'message': message})
            if user.is_active:
                message = 'アクティベーション済みです。'
            if not user.is_active:
                activation_mail(user)
                message = 'アクティベーションメールを再送しました。'
            return render(request, 'registration/resend_activation_email.html', {'message': message})
        else:
            message = 'メールアドレスを入力してください。'
            return render(request, 'registration/resend_activation_email.html', {'form': form, 'message': message})
    else:
        return render(request, 'registration/resend_activation_email.html', {'form': form, 'message': message})


def activation_mail(user):
    if not user.is_active:
        user_activate_token = UserActivateTokens.objects.create(
            user=user,
            expired_at=timezone.now()+timedelta(days=settings.ACTIVATION_EXPIRED_DAYS),
        )
        subject = 'Please Activate Your Account'
        message = f'URLにアクセスしてユーザーアクティベーションを行ってください。\n http://'+os.environ.get("DOMAIN")+f'/accounts/{user_activate_token.activate_token}/activation/'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [
        user.email,
    ]
    send_mail(subject, message, from_email, recipient_list)