# Django To-Do List App 📝

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

A simple, yet powerful to-do list web application built with Django. Manage your tasks with ease using a clean, intuitive interface.

## 🚀 Features

- ✅ **Add Tasks**: Create new tasks with ease
- 👀 **View Tasks**: Display all your tasks in a clean list format
- ✏️ Update Tasks: Edit and modify existing tasks
- 🗑️ **Delete Tasks**: Remove completed or unwanted tasks
- 🎨 **Simple UI**: Clean HTML templates for better user experience
- 💾 **Persistent Storage**: SQLite database for reliable data storage

## 🛠️ Tech Stack

- 🐍 **Backend**: Django (Python web framework)
- 🗄️ **Database**: SQLite (lightweight, file-based database)
- 🦄 **WSGI Server**: Gunicorn (Python WSGI HTTP Server)
- 🌐 **Web Server**: Nginx (reverse proxy & static file server)
- 🎨 **Frontend**: HTML templates with Django templating engine

## 📁 Project Structure

```
todo_project/
├── todo_project/
│   ├── __init__.py
│   ├── settings.py          # Django settings configuration
│   ├── urls.py             # Main URL routing
│   ├── wsgi.py             # WSGI configuration for deployment
│   └── asgi.py             # ASGI configuration (optional)
├── tasks/
│   ├── __init__.py
│   ├── admin.py            # Django admin configuration
│   ├── apps.py             # App configuration
│   ├── models.py           # Task model definition
│   ├── views.py            # View functions for task operations
│   ├── urls.py             # App-specific URL routing
│   ├── tests.py            # Unit tests
│   ├── migrations/         # Database migrations
│   └── templates/tasks/
│       └── task_list.html  # Main template for task display
├── static/                 # Static files (CSS, JS, images)
├── staticfiles/           # Collected static files (production)
├── manage.py              # Django management script
├── db.sqlite3            # SQLite database file
├── requirements.txt      # Python dependencies
└── README.md            # This file
```
