# todo_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Main views
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('update/', views.update_task, name='update_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    
    # Additional views
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
    
    # API endpoints
    path('api/tasks/', views.api_task_list, name='api_task_list'),
    path('api/add/', views.api_add_task, name='api_add_task'),
]