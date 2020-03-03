from django.urls import path
# from .views import ToDoList
from . import views

app_name = 'mainapp'

urlpatterns = [
    # path('', ToDoList.as_view(), name='list'),
    path('', views.to_do_list, name='list'),
    path('edit/<pk>/', views.edit_task, name='edit_task'),
    path('completed/<pk>/', views.task_completed, name='task_completed'),
    path('delete/<pk>/', views.delete_task, name='delete_task'),

]
