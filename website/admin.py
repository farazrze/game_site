from django.contrib import admin
from .models import *



class Gameadmin(admin.ModelAdmin):
    list_display=['id','name']




admin.site.register(Game,Gameadmin)
admin.site.register(Category)