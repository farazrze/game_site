from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def product(request,pid):
    n_post=Game.objects.filter(id=pid)
    #posts=get_object_or_404(n_post,id=pid)
    context = {'posts':n_post}
    return render(request,'product-details.html',context)

def shop(request):
    post=Game.objects.filter(status=1)
    context={'post':post}
    return render(request,'shop.html',context)

def test(request):
    game=Game.objects.all()
    context={'game':game}
    return render(request,'test.html',context)