from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Thread, Post, Topic
from .forms import ThreadForm 

# Renders signup page

def signupPage(request):

    page = 'signin'

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except: 
            messages.error(request, 'This User does not exist, please check and try again')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Username or password is incorrect, please check and try again')
        
    context = {'page': page}    
    return render(request, 'signup-logon.html', context)


# Renders logout view

def logoutPage(request):
    logout(request)
    return redirect('homepage')


# Registering new account

def registerAccount(request):
    page = 'register'
    return render(request, 'signup-logon.html')


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

@login_required(login_url='signin')
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

@login_required(login_url='signin')
def updateThread(request, pk):
    thread = Thread.objects.get(id=pk)
    form = ThreadForm(instance=thread)

    if request.user != thread.author:
        return HttpResponse('Only thread authors can update existing threads') 

    if request.method == "POST":
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    context = {'form': form}
    return render(request, 'new-thread.html', context)


# View to delete threads

@login_required(login_url='signin')
def deleteThread(request, pk):
    thread = Thread.objects.get(id=pk)

    if request.user != thread.author:
        return HttpResponse('Only thread authors can delete existing threads') 


    if request.method == "POST":
        thread.delete()
        return redirect('homepage')
    return render(request, 'confirm-delete.html', {'obj': thread})    


