from django.urls import path
from forum import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('news/', views.NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/list/', views.PostListView.as_view(), name='post_list'),
    path('post/new/>', views.CreatePostView.as_view(), name='post_new'),
    path('category/<str:category>/', views.CategoryView.as_view(), name='category'),
]