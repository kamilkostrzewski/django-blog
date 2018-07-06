from django.shortcuts import render


def index(request):
    return render(request, 'index.html/')


def sign(request):
    return render(request, 'sign.html/')
