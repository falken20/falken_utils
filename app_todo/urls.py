
from django.urls import path

from . import views

urlpatterns = [
    path('', views.todo_view, name='todo_view'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('update_todo/<int:todo_id>/', views.update_todo, name='form_update_todo'),
    path('save_todo/<int:todo_id>/', views.save_todo, name='save_todo'),
]
