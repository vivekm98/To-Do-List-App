from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
# Create your views here.
def home(request):
    tasks=Task.objects.filter(is_completed =False).order_by('-updated_at')
    task2=Task.objects.filter(is_completed=True)
    context={
        'tasks':tasks,
        'task2':task2
    }
    return render(request,'home.html',context)

def add(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.is_completed=True
    task.save()
    return redirect('home')

def remove(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.is_completed=False
    task.save()
    return redirect('home')

def edit(request,pk):
    get_task=get_object_or_404(Task,pk=pk)
    if request.method=='POST':
        new_task=request.POST['task']
        get_task.task=new_task
        get_task.save()
        return redirect('home')
    else:
        context={
          "get_task":get_task
        }

    return render(request,'edit.html',context)

def delete(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')