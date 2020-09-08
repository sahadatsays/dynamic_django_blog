from django.shortcuts import render
from .models import BlogModel

# Create your views here.

def show(request):
    blogs = BlogModel.objects.all()
    context = {
        "blog":blogs
    }
    return render(request, 'home.html', context)