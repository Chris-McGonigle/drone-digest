from django.shortcuts import render, redirect
from .models import Thread, Post, Topic
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
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
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, "Oops...that didn't work. Please try again.")    

    return render(request, 'signup-logon.html', {'form': form})


# Renders homepage view

def homepage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    threads = Thread.objects.filter(
        Q(subject__subject__icontains=q)|
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    thread_total = threads.count()
    subjects = Topic.objects.all()

    context = {'threads': threads, 'subjects': subjects, 'thread_total': thread_total}    
    return render(request, 'home.html', context)

# Renders list of threads

def threads(request, pk):
    thread = Thread.objects.get(id=pk)
    comments = thread.post_set.all().order_by('-created')
    if request.method == "POST":
        comment = Post.objects.create(
            author=request.user,
            thread=thread,
            body=request.POST.get('post-body')
        )
        return redirect('threads', pk=thread.id)
    context = {'thread': thread, 'comments': comments}        
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


# View to delete posts

@login_required(login_url='signin')
def deleteComment(request, pk):
    comment = Post.objects.get(id=pk)

    if request.user != comment.author:
        return HttpResponse('Only comment authors can delete existing threads') 


    if request.method == "POST":
        comment.delete()
        return redirect('homepage')
    return render(request, 'confirm-delete.html', {'obj': comment})    
