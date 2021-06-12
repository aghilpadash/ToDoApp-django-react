from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'completed', 'created_at')
    ordering = ['id']


admin.site.register(Todo, TodoAdmin)
