from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import TodoItem
import json

def task_list(request):
    """Display all todo items"""
    tasks = TodoItem.objects.all().order_by('-created_at')
    context = {
        'tasks': tasks,
        'total_tasks': tasks.count(),
        'completed_tasks': tasks.filter(completed=True).count(),
        'pending_tasks': tasks.filter(completed=False).count(),
    }
    return render(request, 'todo_app/task_list.html', context)

def add_task(request):
    """Add a new todo item"""
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        
        if title:
            TodoItem.objects.create(
                title=title,
                description=description
            )
            messages.success(request, 'Task added successfully!')
            return redirect('task_list')
        else:
            messages.error(request, 'Title is required!')
    
    return render(request, 'todo_app/add_task.html')

def update_task(request):
    """Update an existing todo item"""
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        completed = request.POST.get('completed') == 'on'
        
        try:
            task = get_object_or_404(TodoItem, id=task_id)
            task.title = title
            task.description = description
            task.completed = completed
            task.save()
            messages.success(request, 'Task updated successfully!')
        except TodoItem.DoesNotExist:
            messages.error(request, 'Task not found!')
    
    return redirect('task_list')

def delete_task(request, task_id):
    """Delete a todo item"""
    try:
        task = get_object_or_404(TodoItem, id=task_id)
        task.delete()
        messages.success(request, 'Task deleted successfully!')
    except TodoItem.DoesNotExist:
        messages.error(request, 'Task not found!')
    
    return redirect('task_list')

def toggle_task(request, task_id):
    """Toggle the completed status of a task"""
    if request.method == 'POST':
        try:
            task = get_object_or_404(TodoItem, id=task_id)
            task.completed = not task.completed
            task.save()
            
            if request.headers.get('Content-Type') == 'application/json':
                return JsonResponse({
                    'success': True,
                    'completed': task.completed,
                    'message': f'Task {"completed" if task.completed else "marked as pending"}'
                })
            else:
                messages.success(request, f'Task {"completed" if task.completed else "marked as pending"}!')
        except TodoItem.DoesNotExist:
            if request.headers.get('Content-Type') == 'application/json':
                return JsonResponse({'success': False, 'message': 'Task not found!'})
            else:
                messages.error(request, 'Task not found!')
    
    return redirect('task_list')

def task_detail(request, task_id):
    """Display detailed view of a specific task"""
    task = get_object_or_404(TodoItem, id=task_id)
    context = {'task': task}
    return render(request, 'todo_app/task_detail.html', context)

def edit_task(request, task_id):
    """Edit a specific task"""
    task = get_object_or_404(TodoItem, id=task_id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        completed = request.POST.get('completed') == 'on'
        
        if title:
            task.title = title
            task.description = description
            task.completed = completed
            task.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('task_detail', task_id=task.id)
        else:
            messages.error(request, 'Title is required!')
    
    context = {'task': task}
    return render(request, 'todo_app/edit_task.html', context)

# API Views for AJAX requests
@csrf_exempt
def api_task_list(request):
    """API endpoint to get all tasks as JSON"""
    if request.method == 'GET':
        tasks = TodoItem.objects.all().order_by('-created_at')
        tasks_data = []
        for task in tasks:
            tasks_data.append({
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'completed': task.completed,
                'created_at': task.created_at.isoformat(),
                'updated_at': task.updated_at.isoformat(),
            })
        return JsonResponse({'tasks': tasks_data, 'count': len(tasks_data)})
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def api_add_task(request):
    """API endpoint to add a new task"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title')
            description = data.get('description', '')
            
            if title:
                task = TodoItem.objects.create(
                    title=title,
                    description=description
                )
                return JsonResponse({
                    'success': True,
                    'task': {
                        'id': task.id,
                        'title': task.title,
                        'description': task.description,
                        'completed': task.completed,
                        'created_at': task.created_at.isoformat(),
                    },
                    'message': 'Task created successfully!'
                })
            else:
                return JsonResponse({'success': False, 'message': 'Title is required!'})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data!'})
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)
