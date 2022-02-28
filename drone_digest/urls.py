from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def homepage(request):
    return HttpResponse('Home Page Test')

def threads(request):
    return HttpResponse('Threads Page Test')    


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('threads/', threads),
]
