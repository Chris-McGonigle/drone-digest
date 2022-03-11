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


def signupPage(request):
    """
    Renders signup page
    """

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



def logoutPage(request):
    """
    Renders logout view
    """
    logout(request)
    return redirect('homepage')



def registerAccount(request):
    """
    Registering new account
    """
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



def homepage(request):
    """
    Renders homepage view
    """
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    threads = Thread.objects.filter(
        Q(subject__subject__icontains=q)|
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    subjects = Topic.objects.all()
    thread_total = threads.count()

    comments = Post.objects.all()

    context = {'threads': threads, 'subjects': subjects, 'thread_total': thread_total, 'comments': comments}    
    return render(request, 'home.html', context)


def threads(request, pk):
    """
    Renders list of threads
    """
    thread = Thread.objects.get(id=pk)
    comments = thread.post_set.all()
    droners = thread.droners.all()
    if request.method == "POST":
        comment = Post.objects.create(
            author=request.user,
            thread=thread,
            body=request.POST.get('post-body')
        )
        thread.droners.add(request.user)
        return redirect('threads', pk=thread.id)
    context = {'thread': thread, 'comments': comments, 'droners':droners}        
    return render(request, 'threads.html', context)



@login_required(login_url='signin')
def newThread(request):
    """
    Renders new thread and sends input to back end
    """
    form = ThreadForm()
    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    context = {'form': form}
    return render(request, 'new-thread.html', context)



@login_required(login_url='signin')
def updateThread(request, pk):
    """
    View to update existing thread
    """
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



@login_required(login_url='signin')
def deleteThread(request, pk):
    """
    View to delete threads
    """
    thread = Thread.objects.get(id=pk)

    if request.user != thread.author:
        return HttpResponse('Only thread authors can delete existing threads') 


    if request.method == "POST":
        thread.delete()
        return redirect('homepage')
    return render(request, 'confirm-delete.html', {'obj': thread})    



@login_required(login_url='signin')
def deleteComment(request, pk):
    """
    View to delete posts
    """
    comment = Post.objects.get(id=pk)

    if request.user != comment.author:
        return HttpResponse('Only comment authors can delete existing threads') 


    if request.method == "POST":
        comment.delete()
        return redirect('homepage')
    return render(request, 'confirm-delete.html', {'obj': comment})    
