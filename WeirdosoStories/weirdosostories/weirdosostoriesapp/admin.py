from django.contrib import admin
from .models import BookPost, Comment, Subscribers


# Register your models here.
admin.site.register(BookPost)
admin.site.register(Comment)
admin.site.register(Subscribers)
