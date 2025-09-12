
---

# Django 4 Blog Project – Capítulo 1

## Resumen del proyecto y entorno

* **Framework:** Django 4.x (MTV: Model-Template-View)

  * **Model:** define datos y lógica de acceso a la base.
  * **Template:** define la presentación de los datos.
  * **View:** recibe solicitudes, consulta modelos y renderiza templates.

* **Filosofía:** DRY (Don't Repeat Yourself), desarrollo rápido y reutilización de código.

* **Características útiles de Django 4:** caching, hash seguro de passwords, renderizado de formularios, soporte ASGI y ORM asíncrono.

---

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

---

## Estructura del proyecto y archivos principales

```
mysite/
├─ manage.py             # Comando para interactuar con Django
├─ mysite/
│  ├─ settings.py        # Configuración general del proyecto (apps, middleware, templates, BD, estáticos)
│  ├─ urls.py            # Rutas principales del proyecto
└─ blog/
   ├─ models.py          # Modelo Post + manager personalizado
   ├─ views.py           # Lógica de vistas (lista y detalle)
   ├─ admin.py           # Configuración del admin
   ├─ urls.py            # Rutas de la app
   ├─ templates/         # Plantillas HTML
```

> Los demás archivos (`apps.py`, `tests.py`, `migrations/`) se usan como soporte o para pruebas/migraciones.

---

## Archivos `.py` usados

* `mysite/settings.py` → configuración general: apps instaladas, middleware, templates, base de datos SQLite, archivos estáticos, zona horaria, idioma, validadores de password.
* `mysite/urls.py` → define rutas principales y conecta la app `blog` con su namespace.
* `blog/models.py` → define `Post` y el manager `published` para filtrar solo posts publicados.
* `blog/views.py` → define vistas `post_list` y `post_detail` que renderizan templates.
* `blog/admin.py` → registro de modelo `Post`, con filtros, búsqueda, campos automáticos y ordenación.
* `blog/urls.py` → rutas de la app (lista y detalle).

---

## Conceptos importantes

* **Manager personalizado:** `Post.published.all()` devuelve solo posts publicados.
* **Meta de modelos:** orden descendente por fecha y uso de índices para optimizar consultas.
* **Migraciones:** Django crea automáticamente PK (`id`) y permite ver SQL antes de aplicarlas (`sqlmigrate`).
* **Admin:** permite gestionar posts y usuarios; se configuran filtros, búsqueda y campos prepopulados.
* **Templates:** `{% block content %}` se rellena según la vista, `{% load static %}` permite usar CSS/JS.
* **Request/Response cycle:**

  1. Navegador solicita URL.
  2. Django identifica la vista.
  3. Vista consulta el modelo y renderiza el template.
  4. Retorna `HttpResponse` con HTML.

---

## Templates (resumen)

* **`base.html`** → plantilla base con bloques (`title`, `content`) y sidebar.
* **`list.html`** → lista de posts usando `{% for post in posts %}`; muestra título, autor, fecha y resumen.
* **`detail.html`** → detalle de un post; muestra contenido completo.

> Para más detalle, ver comentarios línea por línea en los archivos del repo.

---
# Django 4  Project – Capítulo 2
## Resumen del proyecto y entorno

