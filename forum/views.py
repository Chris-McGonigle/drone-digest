from django.shortcuts import render

def homepage(request):
    return render (request, 'base.html')

def threads(request):
    return render (request, 'threads.html')
