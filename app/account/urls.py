from django.urls import path
from django.views.generic import TemplateView
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('delete_confirm', TemplateView.as_view(template_name='registration/delete_confirm.html'), name='delete-confirmation'),
    path('delete_complete', DeleteView.as_view(), name='delete-complete'),
    path('<uuid:activate_token>/activation/', activate_user, name='users-activation'),
    path('resend_activation/', resend_activation_email, name='resend-activation'),
    path('before_activation/', BeforeActivation.as_view(), name='before-activation'),

]