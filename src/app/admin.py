from django.contrib import admin
from .models import BuildVersion, Change

@admin.register(BuildVersion)
class BuildVersionAdmin(admin.ModelAdmin):
    list_display = ('version_number', 'date_created')


@admin.register(Change)
class ChangeAdmin(admin.ModelAdmin):
    list_display = ('author_username', 'author_url',
                    'description', 'pr_url',
                    'pr_number', 'category',
                    'date_added', 'build')