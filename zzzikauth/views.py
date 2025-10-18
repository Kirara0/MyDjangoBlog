from email.policy import default
from django.contrib.auth import get_user_model, login, logout
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
import string
import random
from django.core.mail import send_mail
from django.urls import reverse

from .models import CaptchaModel
from django.views.decorators.http import require_http_methods
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User

from MyDjangoBlog import settings

User = get_user_model()


# Create your views here.
@require_http_methods(["GET", "POST"])
def zzz_login(request):
    if request.method == "GET":
        return render(request, 'html/login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']
            user = User.objects.get(username=username)
            if user and user.check_password(password):
                # 登录用户
                login(request, user)
                # 判断是否已登录
                # user.is_authenticated
                # 记住登录状态
                if remember_me:
                    request.session.set_expiry(60 * 60 * 24 * 7)  # 7天
                else:
                    request.session.set_expiry(0)  # 浏览器关闭时过期
                return redirect(reverse('blog:index'))
            else:
                print('登录失败')
                form.add_error('username', '用户名或密码错误')
                # return render(request, 'html/login.html', {'form': form})
                return redirect(reverse('zzzikauth:zzz_login'))


def user_logout(request):
    # 退出登录
    logout(request)
    # request.session.clear()
    return redirect(reverse('zzzikauth:zzz_login'))


@require_http_methods(["GET", "POST"])
def register(request):
    if request.method == "GET":
        return render(request, 'html/register.html')
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # 创建用户
            User.objects.create_user(username=username, email=email, password=password)
            return redirect(reverse('zzzikauth:zzz_login'))
        else:
            print(form.errors)
            # 注册失败重新跳转到注册界面
            return render(request, 'html/register.html', {'form': form})


def send_email_captcha(request):
    # 发送验证码邮件
    email = request.GET.get('email')
    if not email:
        return JsonResponse({'code': 400, 'message': '邮箱不能为空'})
    # 生成验证码（六位数字）
    captcha = ''.join(random.choices(string.digits, k=6))
    # 保存验证码到数据库(如果存在则更新，否则创建)
    CaptchaModel.objects.update_or_create(email=email, defaults={'captcha': captcha})
    send_mail("绳网注册验证码", message=f"您的验证码为{captcha}", recipient_list=[email],
              from_email=settings.EMAIL_HOST_USER)
    return JsonResponse({'code': 200, 'message': '验证码发送成功'})
