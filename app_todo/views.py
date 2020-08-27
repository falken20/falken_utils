from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import logging
import os

from .models import TodoItem


def todo_view(request):
    """Show all the todo tasks"""
    all_todo_items = TodoItem.objects.all().order_by('date_created')
    return render(request, 'todo/todo.html', {'all_items': all_todo_items})


def add_todo(request):
    """Create a new todo task"""
    TodoItem(content=request.POST['content']).save()
    logging.info(f'{os.getenv("ID_LOG", "")} Todo task successfully added')
    # Redirect to the app_todo page
    return HttpResponseRedirect('/todo/')


def delete_todo(request, todo_id):
    """Delete one todo task"""
    logging.info(f'{os.getenv("ID_LOG", "")} Deleting the element with id={todo_id}')
    TodoItem.objects.get(id=todo_id).delete()
    logging.info(f'{os.getenv("ID_LOG", "")} Todo task with id={todo_id} successfully deleted')
    # Redirect to the app_todo page
    return HttpResponseRedirect('/todo/')


def update_todo(request, todo_id):
    """
    This method look for an id and show thr form with the data to update
    :param request:
    :param todo_id: ID task to show for updating
    """
    logging.info(f'{os.getenv("ID_LOG", "")} Showing the form to update the task with id={todo_id}')

    todo_item = TodoItem.objects.get(id=todo_id)

    return render(request, 'todo/todo_form.html', {'todo_item': todo_item})


def save_todo(request, todo_id):
    """ This method updates the task from the edit form """

    logging.info(f'{os.getenv("ID_LOG", "")} Starting to update the task with id={todo_id}')

    todo_item = TodoItem.objects.get(id=todo_id)

    if todo_item:
        todo_item.content = request.POST['todo_content']
        todo_item.save()
        logging.info(f'{os.getenv("ID_LOG", "")} Todo task with id={todo_id} successfully updated')
    else:
        logging.error(f'{os.getenv("ID_LOG", "")} Todo task with id={todo_id} doesnt exist')

    return HttpResponseRedirect('/todo/')





