
from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated', 'timestamp']
    ordering = ['timestamp']
    list_filter = ['timestamp', 'updated']
    search_fields = ['title', 'content']

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)