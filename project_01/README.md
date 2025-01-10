# Project 1 - Views and Templates in Django

## How are views created?
Create a new file called `views.py`
```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World :)")
```

## How to configure paths in `urls.py`
```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_us, name='contact')
]
```

## How to return HTML response from `views`?
- Define the HTML file at `project/templates/website/index.html`
- Go to `settings.py` and set the TEMPLATES directory
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Set template diretctory here
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
- Import the `render` method from `django.shortcuts`
```python
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello World :)")
    return render(request, template_name='website/index.html')
```

## How to include CSS?
- Create a new folder called `static` and add the `style.css` file
- Go to `index.html` file and add the following
```html
{% load static %}   <!-- required to be imported to load static elements -->
<head>
    <!-- static keyword is used to load static asset -->
    <link rel="stylesheet" href="{% static 'style.css' %}">
</head>
```
- Then go to `settings.py` and add `STATICFILES_DIRS` setting
``` python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
```

# Create Apps
- Create the app with the following command - `python manage.py startapp [app-name]`
- Add the said app in settings.py
```python
INSTALLED_APPS = [
    ...
    'Base'
]
```
- Create a new folder for `templates` in `Base` App
- Inside the templates folder, create another folder with the same name as the project (here Base).
- Finally create a file called `all_base.html`
- Create a view
- Then, copy the contents from urls.py and create a `new urls.py` in the Base folder.

# How to use Layouts?
- Create a new file called `layout.html` in the templates folder under main project
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
        {% block title %}
        Default Value
        {% endblock title %}
    </title>
    <link rel="stylesheet" href="{% static 'style.css' %}">
    <!-- static keyword is used to load static asset -->
</head>
<body>
    <nav>This is our navbar</nav>
    {% block content %}{% endblock content %}
</body>
</html>
```
- Then we can use the `extends` keyword to include the layout
### `index.html`
```html
{% extends "layout.html" %}

{% block title %}
Chai Aur Django
{% endblock title %}

{% block content %}
<h1>Chai aur Django | Homepage</h1>
    <h1><a href="about/">About Us</a></h1>
    <h1><a href="contact/">Contact Us</a></h1>
    <h1><a href="chai/">Chai</a></h1>
{% endblock content %}
```

# Migrations and Admin Panel
- `python manage.py migrate`
- Create superuser using the following command to use the Admin Panel
    - `python manage.py createsuperuser`
    - Set username and password