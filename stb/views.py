import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

# Create your views here.

def about(request):
    return render(request, 'stb/about.html')

def blog(request):
    return render(request, 'stb/blog.html')

def contact(request):
    return render(request, 'stb/contact.html')

def index(request):
    return render(request, 'stb/index.html')

def jjb(request):
    return render(request, 'stb/jjb.html')
