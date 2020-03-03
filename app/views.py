from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import ThingToDo
from .forms import TaskForm


def to_do_list(request):
    tasks = ThingToDo.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')


    context = {'tasks': tasks}

    return render(request, 'app/list.html', context)


def edit_task(request, pk):
    task = ThingToDo.objects.get(id=pk)

    if request.method == 'POST':
        #  without instance=task it would create a new tasks
        #  adding that parameter I tell Django to use the request.POST data to overwrite the current value of the atsk
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()

        return redirect('/')

    is_active = True
    context = {'task': task, 'is_active': is_active}

    return render(request, 'app/list.html', context)


def task_completed(request, pk):
    task = ThingToDo.objects.get(id=pk)
    task.completed = True
    task.save()

    return redirect('/')


def delete_task(request, pk):
    task = ThingToDo.objects.get(id=pk)
    task.delete()

    return redirect('/')
