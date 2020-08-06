from django.shortcuts import render,redirect
from .forms import TaskForm
from .models import Task

# Create your views here.

def index(request):
    tasks=Task.objects.all()

    form=TaskForm()
    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    content={'tasks':tasks,'form':form}

    return render(request,'todo/index.html',content)

def updateTodo(request,id):
    task=Task.objects.get(id=id)
    form=TaskForm(instance=task)

    if request.method=="POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    content={'form':form}
    return render(request,'todo/update.html',content)


def deleteTodo(request,id):
    item = Task.objects.get(id=id)
    if request.method=='POST':
        item.delete()
        return redirect('/')

    context={'item':item}
    return render(request,'todo/delete.html',context)