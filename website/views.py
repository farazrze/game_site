from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def product(request):
    return render(request,'product-details.html')

def shop(request):
    return render(request,'shop.html')