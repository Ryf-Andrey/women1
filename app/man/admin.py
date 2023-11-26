from django.contrib import admin

from .models import *

# Register your models here.

class ManAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')  #search_fields = ('title',)   запятая обязательно потому что кортеж
    list_editable = ('is_published', 'photo')  #редактируем поле
    list_filter = ('is_published', 'time_create') # фитровать список (сайт бар с боку)

admin.site.register(Man, ManAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )  #search_fields = ('title',)   запятая обязательно потому что кортеж
    

admin.site.register(Category, CategoryAdmin)