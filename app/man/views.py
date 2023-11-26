from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect
# Create your views here.
from .models import *


menu = [
    {
        'title': "О сайте", 'url_name': 'about'
    },
    {
        'title': "Добавить статью", 'url_name': 'addpage'
    },
    {
        'title': "Обратная связь", 'url_name': 'contact'
    },
    {
        'title': "Войти", 'url_name': 'login'
    }
]

def index(request):
    cat = Category.objects.all()
    posts = Man.objects.all()
    context = {
        'title': 'Главня страница',
        'menu': menu,
        'posts' : posts,
        'cat' : cat
    }

    return render(request, 'man/index.html', context=context)

def about(request):
    list = {
        'title': 'Про нас'
    }
    return render(request, 'man/about.html', list)


def show_post(request, post_id):
    return HttpResponse(f'1 - {post_id}')




def show_category(request, cat_id):
    posts = Man.objects.filter(cat_id=cat_id)
    cat = Category.objects.all()

    if len(posts) == 0:
        raise Http404()
    

    context = {
        'title': 'Главня страница',
        'menu': menu,
        'posts' : posts,
        'cat' : cat,
        'cat_celected' : cat_id
    }
    
    return render(request, 'man/index.html', context=context)

    










def addpage(request):
    return HttpResponse('Добавить статью')
def contact(request):
    return HttpResponse('Обратная связь')
def login(request, ):
    return HttpResponse('Авторизация')


def pageNotFound(request, exception):
    return HttpResponseNotFound('HOOOOOOOO BBBBBBBBBBBBTTTTTTTTT 404')




def bear(request, year):
    if int(year > 2022):
        return redirect('/', permanent=True)                                         #(301)#302 - permanent
    return HttpResponse(f'yyyyyyyyyyyyyyyyyyyyyyy{year}yyyyyyyyyyyyyyyyyyyyyyy')













