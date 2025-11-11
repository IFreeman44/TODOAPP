from django.contrib import admin
from .models import Todo



class TodoAdmin(admin.ModelAdmin):
    model = Todo
    list_display = ['id', 'todo_date', 'todo_name',]

admin.site.register(Todo, TodoAdmin)
