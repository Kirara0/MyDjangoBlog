from django import forms
from django.contrib.auth import get_user_model
from .models import CaptchaModel
User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=7, min_length=2, label="用户名",
                               error_messages={"required": "用户名不能为空", "max_length": "用户名最多7个字符",
                                               "min_length": "用户名最少2个字符"})
    email = forms.EmailField(max_length=20, min_length=6, label="邮箱",
                             error_messages={'invalid': '请传入正确的邮箱格式'})
    password = forms.CharField(max_length=20, min_length=6, label="密码",
                               error_messages={"required": "密码不能为空", "max_length": "密码最多20个字符",
                                               "min_length": "密码最少6个字符"})
    captcha = forms.CharField(max_length=6, min_length=6, label="验证码",
                              error_messages={"required": "验证码不能为空", "max_length": "验证码最多6个字符",
                                              "min_length": "验证码最少6个字符"})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError("邮箱已注册")
        return email

    def clean_captcha(self):
        captcha = self.cleaned_data.get('captcha')
        email = self.cleaned_data.get('email')

        captcha_model = CaptchaModel.objects.get(email=email,captcha=captcha)
        if not captcha_model:
            raise forms.ValidationError("验证码错误")
        captcha_model.delete()
        return captcha


class LoginForm(forms.Form):
    username = forms.CharField(max_length=7, min_length=2,)
    password = forms.CharField(max_length=20, min_length=6,)
    remember_me = forms.IntegerField(required=False)