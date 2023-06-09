from django.contrib import admin
from tasks.models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'priority', 'description')


admin.site.register(Task, TaskAdmin)
