from .models import News, SmallCategory, MiddleCategory, LargeCategory, Category
def common(request):
    large_list = LargeCategory.objects.all()
    middle_list = MiddleCategory.objects.all()
    small_list = SmallCategory.objects.all()
    category_list = Category.objects.all()
    
    context = {
        'large_list': large_list,
        'middle_list': middle_list,
        'small_list': small_list,
        'category_list': category_list,
        'news_list': News.objects.order_by('-created_date')[:3],
    }
    return context