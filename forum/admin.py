from django.contrib import admin
from .models import News, Post, LargeCategory, MiddleCategory, SmallCategory, Category, Comment

# Register your models here.
admin.site.register(News)
admin.site.register(LargeCategory)
admin.site.register(MiddleCategory)
admin.site.register(SmallCategory)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)