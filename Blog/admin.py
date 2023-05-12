from django.contrib import admin
from .models import *



class PostAdmin(admin.ModelAdmin):
        list_display = ["title", "author", "date_posted"]

admin.site.register(Post, PostAdmin)