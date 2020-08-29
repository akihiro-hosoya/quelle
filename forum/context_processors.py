from .models import Post, News
# SmallCategory, MiddleCategory, LargeCategory, Category, 
def common(request):
    context = {
        # 'large_list': Category.large.objects.all(),
        # 'middle_list': Category.middle.objects.all(),
        # 'small_list': Category.small.objects.all(),
        # 'category_list': Category.objects.all(),
        'news_list': News.objects.order_by('-created_date')[:3],
    }
    return context