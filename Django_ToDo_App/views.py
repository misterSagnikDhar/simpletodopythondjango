from django.shortcuts import render, redirect
# from django.contrib import messages
from .models import Task
from .forms import TaskForm


# Create your views here.
def index(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    tasks = Task.objects.all()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'index.html', context)


# noinspection PyPep8Naming
def updateTask(request, task_id):
    task = Task.objects.get(id=task_id)
    task.status = True
    task.save()
    return redirect('home')


# noinspection PyPep8Naming
def deleteTask(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')
