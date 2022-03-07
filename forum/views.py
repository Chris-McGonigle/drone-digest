from django.shortcuts import render, redirect
from .models import Thread, Post, Topic
from .forms import ThreadForm 

# Renders signup page

def signupPage(request):
    context = {}    
    return render(request, 'signup-logon.html', context)


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
    form = ThreadForm()
    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    context = {'form': form}
    return render(request, 'new-thread.html', context)


# View to update existing thread

def updateThread(request, pk):
    thread = Thread.objects.get(id=pk)
    form = ThreadForm(instance=thread)
    if request.method == "POST":
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    context = {'form': form}
    return render(request, 'new-thread.html', context)


# View to delete threads

def deleteThread(request, pk):
    thread = Thread.objects.get(id=pk)
    if request.method == "POST":
        thread.delete()
        return redirect('homepage')
    return render(request, 'confirm-delete.html', {'obj': thread})    


