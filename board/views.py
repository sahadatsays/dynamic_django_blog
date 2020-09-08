from django.shortcuts import render
from .models import BlogModel, NavMenu, PrimaryNav
from menu import Menu, MenuItem

# Create your views here.

def show(request):
    blogs = BlogModel.objects.all()
    # navs = NavMenu.objects.all()
    navs = PrimaryNav.objects.filter()
    context = {
        "blog":blogs,
        "navs": navs,
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {})
def contact(request):
    return render(request, 'contact.html', {})