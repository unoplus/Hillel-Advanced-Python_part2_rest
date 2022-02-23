from django.contrib import admin

from .models import HealthCheck, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "created_at",
        "updated_at",
    )
    search_fields = ("title",)
    list_filter = ("author", "updated_at")
    ordering = ("-updated_at",)


@admin.register(HealthCheck)
class HealthCheckAdmin(admin.ModelAdmin):
    pass
