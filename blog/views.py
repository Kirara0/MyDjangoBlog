from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    return render(request, 'html/index.html')


def blog_detail(request, blog_id):
    return render(request, 'html/detail.html')


# 在settings添加LOGIN_URL = '/auth/login/'后，登录装饰器可以直接使用LOGIN_URL
@login_required(login_url=reverse_lazy('zzzikauth:zzz_login'))  # 登录装饰器，未登录用户跳转到登录页面（懒加载）
def blog_public(request):
    return render(request, 'html/public.html')
