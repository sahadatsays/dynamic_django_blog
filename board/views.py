from django.shortcuts import render, get_object_or_404
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
    return render(request, 'pages/home.html', context)


def page(request, slug):
    page_content = get_object_or_404(BlogModel, slug = slug)
    return render(request, 'pages/page.html', {
        'page_content': page_content, 
        'navs': PrimaryNav.objects.filter()
        })



def about(request):
    return render(request, 'about.html', {})
def contact(request):
    return render(request, 'contact.html', {})