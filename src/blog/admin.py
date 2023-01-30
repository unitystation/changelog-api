from django.contrib import admin
from .models import Post, Section
class SectionAdmin(admin.StackedInline):
    model = Section
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("slug__contains",)
    exclude = ('slug',)
    inlines = [SectionAdmin]
