from django import forms
from forum.models import Post, Category
from accounts.models import CustomUser

class PostForm(forms.Form):
    category_data = Category.objects.all()
    category_choice = {}
    for category in category_data:
        category_choice[category] = category

    title = forms.CharField(max_length=50, label='タイトル')
    text = forms.CharField(label='内容', widget=forms.Textarea())
    category = forms.ChoiceField(
        label='カテゴリ',
        widget=forms.Select,
        choices=list(category_choice.items())
        )