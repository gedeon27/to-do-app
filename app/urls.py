from django.urls import path
# from .views import ToDoList
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<pk>/', views.edit_task, name='edit_task'),
    path('completed/<pk>/', views.task_completed, name='task_completed'),
    path('delete/<pk>/', views.delete_task, name='delete_task'),
    path('signup/', views.signupPage, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

]
