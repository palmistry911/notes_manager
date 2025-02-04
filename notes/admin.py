from django.contrib import admin
from .models import Note


@admin.register(Note)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'updated_at',)
    search_fields = ('title', 'description',)
    list_filter = ('user',)
    ordering = ('-updated_at',)
