from django.shortcuts import render, redirect

def home(request):
    welcome = "Welcome to ABC Musical Store"
    return render(request, 'index/home.html', {'welcome' : welcome})

def author(request):
    author = "Hanjungwon"
    return render(request, 'index/author.html', {'author' : author})

