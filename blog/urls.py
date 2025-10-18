from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('index/', views.index, name='index'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('public/', views.blog_public, name='blog_public'),
]
