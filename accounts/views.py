from django.shortcuts import render, redirect
from django.views import View
from accounts.models import CustomUser

# Create your views here.
class ProfileView(View):
    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)

        return render(request, 'accounts/profile.html', {
            'user_data': user_data,
        })