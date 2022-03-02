from django.shortcuts import render


def homepage(request):
    return render (request, 'home.html')


def threads(request):
    return render (request, 'threads.html')
