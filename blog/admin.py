from django.contrib import admin
from .models import Blog, BlogCategory, BlogComment
# Register your models here.

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BlogAdmin(admin.ModelAdmin):
    list_display = ['category', 'author', 'content', 'title', 'pub_date']


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['blog', 'author', 'content', 'pub_date']


admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)

