from django.contrib import admin
from django.urls import path
from forum import views

urlpatterns = [
    path('logon/', views.signupPage, name="signin"),
    path('logout/', views.logoutPage, name="logout"),
    path('register/', views.registerAccount, name="register"),

    path('admin/', admin.site.urls),

    path('', views.homepage, name="homepage"),
    path('threads/<str:pk>', views.threads, name="threads"),
    path('new-thread/', views.newThread, name="new-thread"),
    path('update-thread/<str:pk>', views.updateThread, name="update-thread"),
    path('delete-thread/<str:pk>', views.deleteThread, name="delete-thread"),
    path('delete-comment/<str:pk>', views.deleteComment, name="delete-comment"),
]
