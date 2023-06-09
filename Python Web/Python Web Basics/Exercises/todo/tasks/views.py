from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):

    context = {
        'tasks': list(Task.objects.all()),
        'form': TaskForm()
    }

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')

    return render(request, 'tasks/list.html', context=context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'tasks/update_task.html', context=context)

def delete_task(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {
        'item': item
    }
    return render(request, 'tasks/delete.html', context=context)
