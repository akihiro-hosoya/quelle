from django.contrib import admin
from .models import News, LargeCategory, MiddleCategory, SmallCategory, Post

# Register your models here.
admin.site.register(News)
admin.site.register(LargeCategory)
admin.site.register(MiddleCategory)
admin.site.register(SmallCategory)
admin.site.register(Post)