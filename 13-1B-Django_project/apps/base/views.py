from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    title = "Geeks"
    settings = Settings.objects.latest('id')
    return render(request, 'base/index.html', locals())

def contact(request):
    settings = Settings.objects.latest('id')
    return render(request, 'base/contact.html', locals())

def home_two(request):
    settings = Settings.objects.latest('id')
    return render(request, 'home-two.html', locals())

def home_three(request):
    settings = Settings.objects.latest('id')
    return render(request, 'home-three.html', locals())

def blog_details(request):
    settings = Settings.objects.latest('id')
    return render(request, 'blog/blog-details.html', locals())

