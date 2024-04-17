from django.shortcuts import render
from .models import *

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def product(request):
    return render(request,'product-details.html')

def shop(request):
    return render(request,'shop.html')

def test(request):
    game=Game.objects.all()
    context={'game':game}
    return render(request,'test.html',context)