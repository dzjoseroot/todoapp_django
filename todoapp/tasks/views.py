from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    tasks = Task.objects.all().order_by('-id')
    form = TaskForm()

    if request.method == 'POST':
        dataForm = TaskForm(request.POST)
        if(dataForm.is_valid()):
            dataForm.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'index.html', context)

def editTask(request, pk):
    task = Task.objects.get(id = pk)
    form = TaskForm(instance = task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance = task)
        if(form.is_valid()):
            form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'edit_task.html', context)

def deleteTask(request, pk):
    task = Task.objects.get(id = pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'item': task}
    return render(request, 'delete_task.html', context)
