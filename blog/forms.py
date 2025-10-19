from django import forms
from .models import Blog, BlogCategory


class PubBlogForm(forms.ModelForm):
    title = forms.CharField(min_length=4, max_length=100)
    content = forms.CharField(min_length=1, widget=forms.Textarea)

    class Meta:
        model = Blog  # 明确关联 Blog 模型
        fields = ['title', 'content', 'category']
