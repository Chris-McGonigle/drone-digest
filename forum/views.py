from django.shortcuts import render, redirect
from .models import Thread, Post, Topic
from .forms import ThreadForm 

# Renders homepage view

def homepage(request):
    threads = Thread.objects.all()
    context = {'threads': threads}    
    return render(request, 'home.html', context)

# Renders list of threads

def threads(request, pk):
    thread = Thread.objects.get(id=pk)
    context = {'thread': thread}        
    return render(request, 'threads.html', context)

# Renders new thread and sends input to back end

def newThread(request):
    thread = ThreadForm()
    if request.method == "POST":
        thread = ThreadForm(request.POST)
        if thread.is_valid():
            thread.save()
            return redirect('homepage')
    context = {'thread': thread}
    return render(request, 'new-thread.html', context) 