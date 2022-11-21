from django.urls import path
from .views import  list_tasks, create_tasks,delete_task

urlpatterns=[
    #al ejecutar la la aplicacion, ejecuta prieramente nuestro html
    path('',list_tasks),
    path('new/', create_tasks, name='create_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
]