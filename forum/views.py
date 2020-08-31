from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import News, Post, LargeCategory, MiddleCategory, SmallCategory, Category, Comment
from .forms import PostForm, CommentForm
from accounts.models import CustomUser
from django.db.models import Q
from functools import reduce
from operator import and_

# Create your views here.
class IndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.all()
        return render(request, 'forum/index.html', {
            'post_data': post_data
        })

class SearchView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.order_by('-id')
        keyword = request.GET.get('keyword')

        if keyword:
            exclusion_list = set([' ', '　'])
            query_list = ''
            for word in keyword:
                if not word in exclusion_list:
                    query_list += word
            query = reduce(and_, [Q(title__icontains=q) | Q(content__icontains=q) for q in query_list])
            post_data = post_data.filter(query)

        return render(request, 'forum/result.html', {
            'keyword': keyword,
            'post_data': post_data
        })

class PostListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.order_by("-id")
        return render(request, 'forum/post_list.html', {
            'post_data': post_data
        })

class CategoryView(View):
    def get(self, request, *args, **kwargs):
        largecategory = LargeCategory.objects.get(name=self.kwargs['largecategory'])
        middlecategory = MiddleCategory.objects.get(name=self.kwargs['middlecategory'])
        smallcategory = SmallCategory.objects.get(name=self.kwargs['smallcategory'], middle=middlecategory)
        category = Category.objects.get(large=largecategory, middle=middlecategory, small=smallcategory)
        post_data = Post.objects.order_by('-id').filter(category=category)
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
            post_data.content = form.cleaned_data['content']
            category = form.cleaned_data['category']
            category_data = Category.objects.get(name=category)
            post_data.category = category_data
            post_data.save()
            return redirect('post_detail', post_data.id)

        return render(request, 'forum/post_form.html', {
            'form': form
        })

class PostEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        form = PostForm(
            request.POST or None,
            initial = {
                'title': post_data.title,
                'category': post_data.category,
                'content': post_data.content,
            }
        )
        return render(request, 'forum/post_form.html', {
            'form': form,
        })
    
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        if form.is_valid():
            post_data = Post.objects.get(id=self.kwargs['pk'])
            post_data.title = form.cleaned_data['title']
            category = form.cleaned_data['category']
            category_data = Category.objects.get(name=category)
            post_data.category = category_data
            post_data.content = form.cleaned_data['content']
            post_data.save()
            return redirect('post_detail', self.kwargs['pk'])

        return render(request, 'forum/post_form.html', {
            'form': form
        })

class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'forum/post_delete.html', {
            'post_data': post_data,
        })
    
    def post(self, request, *args, **kwargs):
            post_data = Post.objects.get(id=self.kwargs['pk'])
            post_data.delete()
            return redirect('post_list')

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

class PreviousPostView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)
        post_list = Post.objects.filter(author=user_data).order_by('created_date')
        return render(request, 'forum/previous_post.html', {
            'user_data': user_data,
            'post_list': post_list,
        })

def post_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'forum/comment_form.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)