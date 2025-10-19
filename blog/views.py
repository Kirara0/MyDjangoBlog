from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from .models import BlogCategory, Blog, BlogComment
from .forms import PubBlogForm


# Create your views here.
def index(request):
    return render(request, 'html/index.html')


def blog_detail(request, blog_id):
    return render(request, 'html/detail.html')


# 在settings添加LOGIN_URL = '/auth/login/'后，登录装饰器可以直接使用LOGIN_URL
@require_http_methods(['GET', 'POST'])
@login_required(login_url=reverse_lazy('zzzikauth:zzz_login'))  # 登录装饰器，未登录用户跳转到登录页面（懒加载）
def blog_public(request):
    if request.method == 'GET':
        categories = BlogCategory.objects.all()
        return render(request, 'html/public.html', context={'categories': categories})
    else:
        print(">>> Received POST data:", dict(request.POST))  # 👈 打印收到的数据
        print(">>> Is 'content' in POST?", 'content' in request.POST)
        print(">>> Content value:", repr(request.POST.get('content')))
        form = PubBlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            category = form.cleaned_data.get('category')
            blog = Blog.objects.create(title=title, content=content, category_id=category.id, author=request.user)
            return JsonResponse({'code': 200, 'msg': '发布成功', 'id': blog.id})
        else:
            print(form.errors)
            return JsonResponse({'code': 400, 'msg': '发布失败'})
