from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class BlogCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 博客
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name


# 博客评论
class BlogComment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog,related_name='comments_set', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:20]

    class Meta:
        verbose_name = '博客评论'
        verbose_name_plural = verbose_name
