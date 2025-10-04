from django.contrib import admin
from .models import DiaryEntry

# Register your models here.

class DiaaryEntryAdmin(admin.ModelAdmin):
    list_display=("title","created_at","updated_at")
    search_fields=("title","content")
    list_filter=("created_at","updated_at")
    ordering=("-created_at")
    date_hierarchy="created_at"
    readonly_fields=("created_at","updated_at")