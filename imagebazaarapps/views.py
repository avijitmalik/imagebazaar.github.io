from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from .models import Images
from .models import Category

# Create your views here.

def Home(request):
    category = Category.objects.all()
    images = Images.objects.all()
    context = {
        'images': images,
        'cat': category,
    }
    return render(request,'home.html',context)