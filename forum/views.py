from django.shortcuts import render
from .models import Thread


def homepage(request):
    threads = Thread.objects.all()
    context = {'threads': threads}    
    return render (request, 'home.html', context)


def threads(request, pk):
    thread = Thread.objects.get(id=pk)
    context = {'thread': thread}        
    return render (request, 'threads.html', context)
