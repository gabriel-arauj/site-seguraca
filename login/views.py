from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import UserInseguro, Comment
from django.contrib import messages
import json


def login(request):
    context = {
        'noticias': 'a' 
    }
    return render(request, 'login.html', context)

def login_site_seguro(request):
    if request.method == 'POST':
        user = request.POST.get('user','')
        password = request.POST.get('password','')
        try:
            user = UserInseguro.objects.get(user=user, password=password)
        except:
            user = None
        if user:
            messages.add_message(request, messages.INFO, user)
            return redirect(reverse('site-seguro'))
    context = {
        'message': 'site insguro' 
    }
    return render(request, 'login.html', context)

def login_site_inseguro(request):
    if request.method == 'POST':
        user = request.POST.get('user','')
        password = request.POST.get('password','')
        query = UserInseguro.objects.raw(f"SELECT * FROM login_userinseguro WHERE user='{user}' AND password='{password}'")
        if query:
            user = query[0]
            messages.add_message(request, messages.INFO, user)
            return redirect(reverse('site-inseguro'))
    context = {
        'message': 'site insguro' 
    }
    return render(request, 'login.html', context)


def comentarios_site_seguro(request):
    storage = messages.get_messages(request)
    user = None
    for m in storage:
        user = m
        break
    storage.used = False

    if request.method == 'POST':
        comment = request.POST.get('comment',None)
        if comment:
            comment = Comment(user=user, comment=comment)
            comment.save()
            return redirect(reverse('site-seguro'))

    all_comments = Comment.objects.all()[::-1]
    context = {
        'img':5,
        'site_seguro': True,
        'comments': all_comments,
        'user': user,
        'message': ' essa é uma sessão de comentários segura, pode ficar Tranquilo.😎' 
    }
    return render(request, 'comments.html', context)

def comentarios_site_inseguro(request):
    storage = messages.get_messages(request)
    user = None
    for m in storage:
        user = m
        break
    storage.used = False

    if request.method == 'POST':
        comment = request.POST.get('comment',None)
        if comment:
            comment = Comment(user=user, comment=comment)
            comment.save()
            return redirect(reverse('site-inseguro'))

    all_comments = Comment.objects.all()[::-1]
    context = {
        'img':6,
        'comments': all_comments,
        'user': user,
        'message': ' essa é uma sessão de comentários insegura, CUIDADO!!! 😱' 
    }
    return render(request, 'comments.html', context)