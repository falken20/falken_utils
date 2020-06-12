from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem


def about_view(request):
    return HttpResponse('<h1>by Richi Rod AKA @richionline / falken20</h1>')


def todo_view(request):
    """Show all the todo tasks"""
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo/todo.html', {'all_items': all_todo_items})


def add_todo(request):
    """Create a new todo task"""
    TodoItem(content=request.POST['content']).save()
    # Redirect to the app_todo page
    return HttpResponseRedirect('/todo/')


def delete_todo(request, todo_id):
    """Delete one todo task"""
    print('ROD: Deleting the element with id=%s', todo_id)
    TodoItem.objects.get(id=todo_id).delete()
    # Redirect to the app_todo page
    return HttpResponseRedirect('/todo/')
