from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "completion_date", "featured", "updated_at")
    list_filter = ("category", "featured")
    search_fields = ("title", "summary", "tools")
    prepopulated_fields = {"slug": ("title",)}
