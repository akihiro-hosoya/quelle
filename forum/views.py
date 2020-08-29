from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import News, Post, LargeCategory, MiddleCategory, SmallCategory
from .forms import PostForm

# Create your views here.
class IndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.all()
        return render(request, 'forum/index.html', {
            'post_data': post_data
        })

class PostListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'forum/post_list.html', {
            'post_data': post_data
        })

class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'forum/post_detail.html', {
            'post_data': post_data
        })

class CreatePostView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        return render(request, 'forum/post_form.html', {
            'form': form,
        })
    
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        if form.is_valid():
            post_data = Post()
            post_data.author = request.user
            post_data.title = form.cleaned_data['title']
            post_data.text = form.cleaned_data['text']
            # category = form.cleaned_data['category']
            # category_data = Category.objects.all
            # post_data.category = category_data
            post_data.save()
            return redirect('forum:post_detail', post_data.id)

        return render(request, 'forum/post_form.html', {
            'form': form
        })

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