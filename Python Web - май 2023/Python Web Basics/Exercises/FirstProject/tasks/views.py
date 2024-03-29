from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import Task

# Create your views here.


def index(request):
    return HttpResponse("It works!")


def list_tasks(request):
    all_tasks = Task.objects.order_by("id").all()
    return HttpResponse(f"{t.id} {t.title} {t.priority}" for t in all_tasks)


def list_tasks_template(request):
    context = {
        "title": 'text',
        "tasks": Task.objects.order_by("id").all()
    }
    return render(request, "tasks/tasks.html", context)
