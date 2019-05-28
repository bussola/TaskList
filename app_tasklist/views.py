from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm, EditTodoForm
import datetime


def index(request):
    todo_list = Todo.objects.order_by('id')
    form = TodoForm()

    context = {
        'todo_list' : todo_list, 
        'form' : form
    }

    return render(request, 'app_tasklist/index.html', context)


@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(titulo=request.POST['titulo'])
        new_todo.save()

    return redirect('index')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.data_conclusao = datetime.datetime.now()
    todo.save()

    return redirect('index')

def inCompleteTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = False
    todo.data_conclusao = None
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index')

def edit(request, todo_id):
    todo_data = Todo.objects.get(pk=todo_id)
    form = EditTodoForm()
    form.fields['edit_titulo'].widget.attrs['placeholder'] = todo_data.titulo
    form.fields['descricao'].widget.attrs['placeholder'] = todo_data.descricao
    context = {
        'todo_data' : todo_data,
        'form': form,
    }

    return render(request, 'app_tasklist/editar.html', context)

@require_POST
def update(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    form = EditTodoForm(request.POST)
    if form.is_valid():
        todo.titulo = request.POST['edit_titulo']
        todo.descricao = request.POST['descricao']
        todo.data_update = datetime.datetime.now()
        todo.save()

    return redirect('index')

def deleteone(request, todo_id):
    todo = Todo.objects.get(pk=todo_id).delete()

    return redirect('index')