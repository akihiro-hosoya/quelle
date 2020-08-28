from django.urls import path
from forum import views

app_name= 'forum'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('news/', views.NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
]