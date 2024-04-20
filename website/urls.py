from django.urls import path
from .views import *

app_name='website'

urlpatterns = [
    path('',index,name='index'),
    path('contact',contact,name='contact'),
    path('shop',shop,name='shop'),
    path('<int:pid>',product,name='product'),
    path('test',test),
    path('category/<str:cat_name>',product,name='category'),
    path('search/',search,name='search')
]