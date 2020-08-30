from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

# 投稿カテゴリ
class LargeCategory(models.Model):
    name = models.CharField('大カテゴリー', max_length=30)
    icon = models.CharField('アイコン', max_length=50)

    def __str__(self):
        return self.name

class MiddleCategory(models.Model):
    name = models.CharField('中カテゴリー', max_length=30)

    def __str__(self):
        return self.name

class SmallCategory(models.Model):
    name = models.CharField('小カテゴリー', max_length=30)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField('カテゴリー', max_length=50)
    large = models.ForeignKey(LargeCategory, verbose_name='大カテゴリー', on_delete=models.PROTECT)
    middle = models.ForeignKey(MiddleCategory, verbose_name='中カテゴリー', on_delete=models.PROTECT)
    small = models.ForeignKey(SmallCategory, verbose_name='小カテゴリー', on_delete=models.PROTECT)

# 投稿
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField("タイトル", max_length=200)
    content = models.TextField("本文")
    created_date = models.DateTimeField("作成日", default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("forum:post_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.title


# NEWS
class News(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title