from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):
    tasks = Task.objects.all()
    context = {'tasks':tasks}
    return render(request, 'app/index.html', context)

def details(request, id):
    task = Task.objects.get(pk=id)
    context = {'task': task}
    return render(request, 'app/details.html', context)

def edit(request, id):
    task = Task.objects.get(id=id)
    context = {'task': task}
    if request.method == "GET":
        return render(request, 'app/edit.html', context)
    elif request.method == "POST":
        # process to save new Task
        task.name = request.POST['name']
        task.description = request.POST['description']
        task.status = request.POST['status']        
        task.save()
        return redirect('/')


def add(request):
    context = {}
    if request.method == "GET":
        return render(request, 'app/add.html')
    elif request.method == "POST":
        # process to save new Task
        name = request.POST['name']
        description = request.POST['description']
        status = request.POST['status']
        task = Task(name=name, description=description, status=status)
        task.save()
        return redirect('/')

def delete(request, id):
    task = Task.objects.get(id=id)
    context = {'task': task}
    if request.method == "GET":
        return render(request, 'app/delete.html', context)
    elif request.method == "POST":
        task.delete()
        return redirect('/')