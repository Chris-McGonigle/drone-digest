from django.shortcuts import render
from .models import Thread, Post, Topic
from .forms import ThreadForm 


def homepage(request):
    threads = Thread.objects.all()
    context = {'threads': threads}    
    return render(request, 'home.html', context)


def threads(request, pk):
    thread = Thread.objects.get(id=pk)
    context = {'thread': thread}        
    return render(request, 'threads.html', context)


def newThread(request):
    thread = ThreadForm()
    context = {'thread': thread}
    return render(request, 'new-thread.html', context) 