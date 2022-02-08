from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at', )
    search_fields = ('title', )
    list_filter = ('author', 'updated_at')
    ordering = ('-updated_at',)


admin.site.register(Post, PostAdmin)
