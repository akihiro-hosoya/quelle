from django.urls import path
from forum import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('news/', views.NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/list/', views.PostListView.as_view(), name='post_list'),
    path('post/new/>', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/>', views.PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/>', views.PostDeleteView.as_view(), name='post_delete'),
    path('category/<str:largecategory>/<str:middlecategory>/<str:smallcategory>/', views.CategoryView.as_view(), name='category'),
    path('previous/post/', views.PreviousPostView.as_view(), name='previous_post'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('post/<int:pk>/comment/', views.post_comment, name='post_comment'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]