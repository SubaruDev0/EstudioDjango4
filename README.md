# Django 4 Blog Project – Capítulo 1

## Resumen del proyecto y entorno

* **Framework:** Django 4.x (MTV: Model-Template-View)
* **Filosofía:** DRY (Don't Repeat Yourself), reutilización de código y desarrollo rápido con Python.
* **Características útiles de Django 4:**

  * Caching con Redis
  * Scrypt password hasher
  * Renderizado de formularios con templates
  * Soporte ASGI y ORM asíncrono

## Setup rápido

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno (Linux/Mac)
source venv/bin/activate

# Activar entorno (Windows)
venv\Scripts\activate

# Instalar Django
pip install django==4.1.0

# Instalar dependencias
pip install -r requirements.txt

# Verificar versión
python3 -m django --version
```

## Ciclo Request/Response

1. El navegador solicita una URL al servidor web.
2. Django compara la URL con los patrones configurados (`urls.py`).
3. Se ejecuta la view correspondiente.
4. La view puede usar modelos para obtener información de la base de datos.
5. La view renderiza un template (HTML) y devuelve un HTTP Response.
6. Middleware puede intervenir en cualquier parte del proceso.

## Estructura del proyecto

```
mysite/
├─ manage.py
├─ mysite/
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
└─ blog/
   ├─ __init__.py
   ├─ admin.py
   ├─ apps.py
   ├─ migrations/
   │  └─ __init__.py
   ├─ models.py
   ├─ tests.py
   └─ views.py
```

* `manage.py`: utilidad para interactuar con el proyecto.
* `settings.py`: configuración del proyecto (DEBUG, ALLOWED\_HOSTS, INSTALLED\_APPS, DATABASES, etc.).
* `urls.py`: define los patrones de URL.
* `models.py`: define los modelos y la estructura de la base de datos.
* `admin.py`: registra modelos para el sitio de administración.

## Aplicaciones vs Proyectos

* **Proyecto:** instalación de Django con configuración y apps.
* **Aplicación:** grupo de modelos, views, templates y URLs que proveen funcionalidades específicas (ej: blog, foro, wiki).

## Creación de la aplicación Blog

```bash
python manage.py startapp blog
```

Archivos generados:

* `__init__.py`: indica que el directorio es un módulo de Python.
* `admin.py`: registrar modelos en el admin.
* `apps.py`: configuración de la app.
* `migrations/`: migraciones de la base de datos.
* `models.py`: definición de modelos.
* `tests.py`: tests de la aplicación.
* `views.py`: lógica de la aplicación.

## Modelo Post

```python
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish'])]

    def __str__(self):
        return self.title
```

* **Campos principales:** title, slug, body, publish, created, updated, status, author.
* **Meta:** ordena por fecha de publicación descendente, agrega índice en `publish`.
* **Status:** enum con `Draft` y `Published`.
* **Relación:** muchos posts pueden pertenecer a un usuario (`author`).

## Migraciones

```bash
# Crear migración inicial de la app blog
python manage.py makemigrations blog

# Ver SQL de la migración
python manage.py sqlmigrate blog 0001

# Aplicar migraciones
python manage.py migrate
```

* Django crea automáticamente un campo `id` autoincremental como PK.
* Índices:

  * Descendente en `publish`.
  * Por defecto en `slug` y `author_id`.

## Administración de Django

```bash
# Crear superusuario
python manage.py createsuperuser
# Luego ingresar username, email y contraseña
```

* Acceder al admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
* Registrar modelos en `admin.py`:

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

* Permite listar, crear, editar y borrar posts de forma sencilla.
* Los formularios se generan automáticamente según los campos del modelo, incluyendo pickers para fechas.

---

Esto cubre **Capítulo 1 – Blog**. El README se puede expandir conforme se agreguen más funcionalidades en capítulos posteriores.
