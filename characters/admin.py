from django.contrib import admin

from .models import Character


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'author', 'updated_at']
    list_filter = ['status']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ['name']}
