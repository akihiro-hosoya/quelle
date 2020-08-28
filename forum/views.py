from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "forum/index.html"
    login_url = '/accounts/login/'