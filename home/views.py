from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


def landing_page(request):
    return render(request, 'landing_page.html')
