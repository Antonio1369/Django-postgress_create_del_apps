from django.shortcuts import render,redirect
from .models import Task

# Create your views here.
#funcion que lee el archivo html
def list_tasks(request):
    #lsita de todos los datos
    tasks=Task.objects.all()
    print(tasks)
    return render(request,'list_tasks.html',{"tasks": tasks})


#recibe los datos y luego los muestra por consola
def create_tasks(request):
    task=Task(titulo=request.POST['title'],foundation =request.POST['foundation'])
    task.save()
    print(request.POST)
    print(request.POST['title'])
    print(request.POST['foundation'])
    return redirect('/tasks/')

def delete_task(request,task_id):
    task = Task.objects.get(id = task_id)
    task.delete()
    return redirect('/tasks/')
