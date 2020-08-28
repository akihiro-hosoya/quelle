from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import News

# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "forum/index.html"
    login_url = '/accounts/login/'

class NewsListView(View):
    def get(self, request, *args, **kwargs):
        news_data = News.objects.order_by("-id")
        return render(request, 'forum/news_list.html', {
            'news_data': news_data,
        })

class NewsDetailView(View):
    def get(self, request, *args, **kwargs):
        news_data = News.objects.get(id=self.kwargs['pk'])
        return render(request, 'forum/news_detail.html', {
            'news_data': news_data,
        })