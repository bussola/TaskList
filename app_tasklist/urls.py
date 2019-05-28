from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('inComplete/<todo_id>', views.inCompleteTodo, name='inComplete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall'),
    path('edit/<todo_id>', views.edit, name='edit'),
    path('update/<todo_id>', views.update, name='update'),
    path('deleteone/<todo_id>', views.deleteone, name='deleteone'),
]
