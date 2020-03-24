from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.utils import timezone
from .models import *
from .forms import *
from .decorators import unauthenticated_user


@unauthenticated_user
def index(request):
    return render(request, 'app/base.html')


def home(request):
    # user_list, created = UserList.objects.get_or_create(user=request.user)
    # tasks = user_list.tasks_listed.all()
    tasks = Task.objects.filter(its_list=request.user)
    context = {'tasks': tasks}

    return render(request, 'app/list.html', context)


def add_task(request):
    user_list, created = UserList.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        task_added = request.POST['thing']
        task = Task.objects.create(thing=task_added, its_list=request.user)
        return redirect('mainapp:home')

    tasks = Task.objects.filter(its_list=request.user)
    context = {'tasks': tasks}

    return render(request, 'app/list.html', context)


def edit_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        #  without instance=task it would create a new tasks
        #  adding that parameter I tell Django to use the request.POST data to overwrite the current value of the atsk
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()

        return redirect('mainapp:home')

    #  LONGER WAY
    # user_list, created = UserList.objects.get_or_create(user=request.user)
    # tasks = user_list.list.all()
    # ------------
    #  SHORTER WAY
    tasks = Task.objects.filter(its_list=request.user)

    is_active = True
    context = {'tasks': tasks, 'task': task, 'is_active': is_active}

    return render(request, 'app/list.html', context)


def task_completed(request, pk):
    #  LONGER WAY
    # task = Task.objects.get(id=pk)
    # task.completed = True
    # task.save()
    # ------------
    #  SHORTER WAY
    task = Task.objects.get(id=pk)
    task.completed = True
    task.save()

    return redirect('mainapp:home')


def delete_task(request, pk):
    #  LONGER WAY
    # task = Task.objects.get(id=pk)
    # task.delete()
    # ------------
    #  SHORTER WAY
    task = Task.objects.filter(id=pk).delete()

    return redirect('mainapp:home')


@unauthenticated_user
def signupPage(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            messages.success(request, f"Welcome {username}")

            return redirect('mainapp:login')

    return render(request, 'app/signup.html')


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            keep_logged = request.POST['remember_me']
        except:
            request.session.set_expiry(0)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('mainapp:home')
        else:
            messages.info(request, "Invalid username or passrowd")

    return render(request, 'app/login.html')


def logoutUser(request):
    logout(request)
    return redirect('/')
