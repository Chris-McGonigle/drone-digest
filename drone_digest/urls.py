from django.contrib import admin
from django.urls import path
from forum import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="homepage"),
    path('threads/<str:pk>', views.threads, name="threads"),
    path('new-thread/', views.newThread, name="new-thread"),
]
