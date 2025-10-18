from django.db import models


# Create your models here.
class CaptchaModel(models.Model):
    email = models.EmailField(error_messages={'invalid': '请输入正确的邮箱格式'}, unique=True)# 邮箱唯一
    captcha = models.CharField(max_length=6)
    create_time = models.DateTimeField(auto_now_add=True)
