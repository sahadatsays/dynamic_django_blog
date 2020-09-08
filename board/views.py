from django.shortcuts import render
from .models import BlogModel, NavMenu
from menu import Menu, MenuItem

# Create your views here.

def show(request):
    blogs = BlogModel.objects.all()
    navs = NavMenu.objects.all()
    context = {
        "blog":blogs,
        "navs": navs
    }
    return render(request, 'home.html', context)