from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, get_list_or_404,redirect
from django.contrib.auth.models import User
from pyexpat.errors import messages
from django.contrib.auth import login, logout, authenticate
from .add_flower import *
from .models import *
# Create your views here.

def index(request: WSGIRequest):
    posts = Lesson.objects.filter(published=True)
    context = {
        "posts": posts,
        "title": "Barcha maqolalar"
    }
    return render(request, "index.html", context)


def posts_by_category(request, category_id):
    posts = get_list_or_404(Lesson, category_id=category_id, published=True)
    category = get_object_or_404(Course, pk=category_id)
    context = {
        'posts': posts,
        "title": f"{category.name}: barcha maqolalar!"
    }
    return render(request, 'index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Lesson, pk=post_id, published=True)
    post.views += 1
    post.save()

    context = {
        "post": post,
        "title": post.title
    }
    return render(request, 'detail.html', context)

def add_flower(request: WSGIRequest):
    if request.method == "POST":
        form = Gullarforms(data=request.POST,files=request.FILES)
        if form.is_valid():
            gul = Lesson.objects.create(**form.cleaned_data)
            return redirect('post_detail',post_id=gul.pk)
    gul = Gullarforms()
    context = {
        "gul":gul
    }
    return render(request,'lesson.html',context)


def update_lesson(request: WSGIRequest, post_id):
    lesson = get_object_or_404(Lesson, pk=post_id)

    if request.method == "POST":
        form = Gullarforms(data=request.POST, files=request.FILES)
        if form.is_valid():
            lesson.title = form.cleaned_data.get('title')
            lesson.content = form.cleaned_data.get('content')
            lesson.photo = form.cleaned_data.get('photo') if form.cleaned_data.get('photo') else lesson.photo
            lesson.category = form.cleaned_data.get('category')
            lesson.published = form.cleaned_data.get('published')
            lesson.save()

    gul = Gullarforms(initial={
        "title":lesson.title,
        "content": lesson.content,
        "photo": lesson.photo,
        "category": lesson.category,
        "published": lesson.published,

    })
    context = {
        "gul":gul,
        "photo":lesson.photo
    }
    return render(request,'lesson.html',context)

def register(request):
    if request.method == "POST":
        form = Registerform(data=request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            password_repeat = form.cleaned_data.get('password_repeat')
            if password_repeat == password:
                user = User.objects.create_user(
                    form.cleaned_data.get('username'),
                    form.cleaned_data.get('email'),
                    password
                )
                return redirect('login')

    context = {
        "form": Registerform()
    }
    return render(request,'auth/register.html',context)

def login_view(request):
    if request.method == "POST":
        form = Loginform(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('home')
    context = {
        "form": Loginform()
    }
    return render(request,'auth/login.html',context)

def logout_view(request):
    logout(request)
    return redirect('login')













