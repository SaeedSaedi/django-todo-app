from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "user",
        "status",
        "created_at",
        "updated_at",
    )  # Fields to display in the list view
    list_filter = ("status", "created_at", "updated_at")  # Filters for the list view
    search_fields = ("title", "user__username")  # Search functionality
    readonly_fields = (
        "created_at",
        "updated_at",
    )  # Make these fields read-only in the admin panel
