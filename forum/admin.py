from django.contrib import admin
from .models import Thread, Post, Topic
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('description')

admin.site.register(Thread)
admin.site.register(Topic)
