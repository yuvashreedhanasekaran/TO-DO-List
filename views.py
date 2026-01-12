from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form})

from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list')

    return render(request, 'update_task.html', {'task': task})

from django.shortcuts import redirect, get_object_or_404
from .models import Task

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

