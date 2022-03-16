from django.contrib import admin
from .models import Thread, Post, Topic
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Thread)
class ThreadAdmin(SummernoteModelAdmin):

    summernote_fields = ('description')
    list_filter = ('subject', 'created')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_filter = ('thread', 'created')

admin.site.register(Topic)
