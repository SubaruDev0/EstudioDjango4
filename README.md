# Proyecto Blog - Django 4 (Capítulo 1)

## Resumen del proyecto y entorno

- Este proyecto utiliza **Django 4.x**, un framework web que sigue el patrón **MTV (Model-Template-View)**.
- Django permite separar claramente las responsabilidades de cada capa:
  - **Model**: maneja la base de datos.
  - **Template**: define la presentación de los datos.
  - **View**: controla la lógica y la interacción del usuario.
- Filosofía principal: **DRY (Don't Repeat Yourself)**, máxima reutilización de código y desarrollo rápido gracias a Python.
- Características nuevas de Django 4 que se pueden aprovechar:
  - **Caching con Redis**: mejora el rendimiento almacenando datos temporales en memoria.
  - **Scrypt password hasher**: almacenamiento seguro de contraseñas.
  - **Renderizado de formularios con templates**: permite personalizar la apariencia de los formularios.
  - **Soporte ASGI y ORM asíncrono**: vistas y consultas asíncronas para aplicaciones con alta concurrencia.

## Setup rápido (recordatorio)

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno (Linux/Mac)
source venv/bin/activate

# Activar entorno (Windows)
venv\Scripts\activate

# Instalar Django
pip install django==4.1.0

# Verificar versión
python3 -m django --version

# Instalar dependencias
pip install -r requirements.txt
````

## Estructura del proyecto

* `mysite/` → contenedor del proyecto:

  * `manage.py` → utilidad de línea de comandos para interactuar con el proyecto.
  * `mysite/` → paquete Python del proyecto:

    * `__init__.py` → indica que es un módulo Python.
    * `asgi.py` → configuración para ASGI (aplicaciones asíncronas).
    * `settings.py` → configuración y ajustes del proyecto.
    * `urls.py` → define las URLs principales.
    * `wsgi.py` → configuración para WSGI (servidores de producción).

## Settings principales (`settings.py`)

* **DEBUG** → `True` en desarrollo, `False` en producción.
* **ALLOWED\_HOSTS** → dominios permitidos cuando `DEBUG=False`.
* **INSTALLED\_APPS** → apps activas (por defecto: admin, auth, sessions, messages, staticfiles).
* **MIDDLEWARE** → lista de middleware ejecutados por request/respuesta.
* **ROOT\_URLCONF** → módulo donde están las URLs raíz.
* **DATABASES** → configuración de la base de datos (por defecto SQLite3).
* **LANGUAGE\_CODE** → idioma por defecto.
* **USE\_TZ** → soporte de zonas horarias.

> 🔗 Documentación completa: [Django Settings](https://docs.djangoproject.com/en/4.1/ref/settings/)

## Creación de una aplicación

* Comando para crear la app `blog`:

```bash
python manage.py startapp blog
```

* Archivos generados:

  * `__init__.py` → marca el directorio como paquete Python.
  * `admin.py` → registrar modelos para admin.
  * `apps.py` → configuración de la app.
  * `migrations/` → migraciones de base de datos.
  * `models.py` → definición de modelos.
  * `views.py` → lógica y vistas.
  * `tests.py` → pruebas unitarias.

## Modelo `Post` (blog)

* Representa las publicaciones del blog.
* Campos:

  * `title` → `CharField`, título del post.
  * `slug` → `SlugField`, URL amigable para SEO (`django-reinhardt-legend-jazz`).
  * `body` → `TextField`, contenido del post.
* Método `__str__()` → devuelve una representación legible del objeto (se ve en admin).
* Django agrega automáticamente un **primary key auto-incremental (`id`)**.

**Ejemplo básico de modelo:**

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title
```

* Proceso para reflejar cambios en la DB:

```bash
python manage.py makemigrations blog
python manage.py migrate
```

* Cada modelo = tabla en la base de datos; cada campo = columna.
* Correspondencia de tipos:

| Campo | Tipo Django | Tipo SQL                |
| ----- | ----------- | ----------------------- |
| title | CharField   | VARCHAR                 |
| slug  | SlugField   | VARCHAR                 |
| body  | TextField   | TEXT                    |
| id    | AutoField   | INT PK auto-incremental |

---

```
```
