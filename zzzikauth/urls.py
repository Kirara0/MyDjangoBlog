from django.urls import path
from . import views

from zzzikauth import views

app_name = 'zzzikauth'
urlpatterns = [
    path('login', views.zzz_login, name='zzz_login'),
    path('logout', views.user_logout, name='logout'),
    path('register', views.register, name='register'),
    path('captcha', views.send_email_captcha, name='captcha'),
]
