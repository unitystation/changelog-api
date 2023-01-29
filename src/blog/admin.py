from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("slug__contains",)
    fields = ("title", "body", "author", 'state', 'type')
