from django.shortcuts import render,redirect
from .forms import TaskForm
from .models import Task
from django.utils import timezone

from django.shortcuts import render, redirect
from .forms import TaskForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

@login_required
def form(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        user=request.user
        if form.is_valid():
            task=form.save(commit=False)
            task.user=request.user
            task.save()
            return redirect('index')
    else:
        form = TaskForm()
    return render(request, "task/form.html", {"form": form})

@require_POST
def delete_task(request,task_id):
    task=Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')

@login_required
def edit_task(request,task_id):
    task=Task.objects.get(id=task_id)
    if request.method=="POST":
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=TaskForm(instance=task)
    return render(request,"task/edit_task.html",{"form":form})

@login_required
def mark_as_done(request,task_id):
    task=Task.objects.get(id=task_id)
    task.status=False
    task.save()
    return redirect('index')