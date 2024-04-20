from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def index(request):
    post=Game.objects.filter(status=1)
    context={'post':post}
    return render(request,'index.html',context)

def contact(request):
    return render(request,'contact.html')


def shop(request,**kwargs):
    post=Game.objects.filter(status=1)
    post=Paginator(post,3)
    try:
        page_number = request.GET.get('page')
        post = post.get_page(page_number)
    except PageNotAnInteger:
        post = post.get_page(1)
    except EmptyPage:
        post = post.get_page(1)
    context={'post':post}
    return render(request,'shop.html',context)

def test(request):
    game=Game.objects.all()
    context={'game':game}
    return render(request,'test.html',context)


def product(request,**kwargs):
    post=Game.objects.filter(status=1)
    if kwargs.get('pid') != None:
        post=post.filter(id=kwargs['pid'])

    if kwargs.get('cat_name') != None:
        post=post.filter(category__name=kwargs['cat_name'])
    context = {'posts':post}
    return render(request,'product-details.html',context)


def search(request):
    post=Game.objects.filter(status=1)
    if request.method=='Get':
        if request.Get.get('s'):
            post.post.filter(name__content=request.Get.get('s'))
    context={'post':post}
    return render(request,'index.html',context)
