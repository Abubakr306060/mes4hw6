from django.shortcuts import render
from apps.base.models import *

# Create your views here.
def blog(request):
    settings = Settings.objects.latest('id')
    return render(request,'blog/blog.html', locals())
