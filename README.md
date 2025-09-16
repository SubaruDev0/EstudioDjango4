
---

# Proyecto Blog - Django 4 (Capítulo 1)

## Resumen del proyecto y entorno

* Este proyecto utiliza **Django 4.x**, framework web que sigue el patrón **MTV (Model-Template-View)**.
* Django separa responsabilidades:

  * **Model:** maneja la base de datos.
  * **Template:** define la presentación de los datos.
  * **View:** controla la lógica y la interacción del usuario.
* Filosofía: **DRY (Don't Repeat Yourself)** → máxima reutilización de código y desarrollo rápido con Python.
* Características de Django 4:

  * **Caching con Redis:** rendimiento mejorado mediante almacenamiento temporal.
  * **Scrypt password hasher:** contraseñas más seguras.
  * **Renderizado de formularios con templates:** permite personalización visual.
  * **Soporte ASGI y ORM asíncrono:** consultas y vistas asíncronas para alta concurrencia.

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

# Verificar versión
python3 -m django --version

# Instalar dependencias
pip install -r requirements.txt
```

---

## Estructura del proyecto

* `mysite/` → contenedor principal:

  * `manage.py` → línea de comandos de Django.
  * `mysite/` → paquete del proyecto:

    * `settings.py` → configuración general (apps, middleware, DB, templates, estáticos).
    * `urls.py` → rutas principales del proyecto.
    * `asgi.py` / `wsgi.py` → configuración para servidores asíncronos y de producción.

* `blog/` → aplicación de blog:

  * `models.py` → definición del modelo `Post` y manager `published`.
  * `views.py` → vistas `post_list` y `post_detail`.
  * `admin.py` → registro y configuración del modelo en el admin.
  * `urls.py` → rutas específicas de la app.
  * `templates/` → plantillas HTML (`base.html`, `list.html`, `detail.html`).
  * `migrations/` → migraciones de base de datos.
  * `tests.py` → pruebas unitarias.
  * `apps.py` → configuración de la app.

> 🔗 Para más detalle línea por línea, ver comentarios en los archivos `.py` del repo.

---

## Settings principales (`settings.py`)

* **DEBUG** → `True` en desarrollo.
* **ALLOWED\_HOSTS** → dominios permitidos en producción.
* **INSTALLED\_APPS** → apps activas (admin, auth, sessions, messages, staticfiles, blog).
* **MIDDLEWARE** → middleware ejecutados por request/respuesta.
* **DATABASES** → configuración de SQLite por defecto.
* **LANGUAGE\_CODE / TIME\_ZONE / USE\_TZ** → internacionalización.

---

## Creación de la app `blog`

```bash
python manage.py startapp blog
```

* Archivos generados: `__init__.py`, `admin.py`, `apps.py`, `migrations/`, `models.py`, `views.py`, `tests.py`.
* Cada archivo cumple funciones específicas para la app y su interacción con Django.

---

## Modelo `Post` (blog)

* Representa publicaciones del blog.
* Campos principales:

  * `title` → título del post.
  * `slug` → URL amigable.
  * `body` → contenido completo.
  * `author`, `status`, `publish`, `created`, `updated`.
* Manager personalizado `published` → filtra automáticamente solo posts publicados.
* Meta → orden descendente por fecha, índice en `publish` para optimizar consultas.

**Fragmento de ejemplo:**

```python
# (Ver código completo en repo para comentarios línea por línea)
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
```

* Django crea automáticamente `id` como PK autoincremental.

---

## Migraciones y DB

```bash
python manage.py makemigrations blog
python manage.py migrate
```

* Cada modelo = tabla; cada campo = columna.
* Tipos de campo Django → correspondencia SQL:

| Campo | Django    | SQL     |
| ----- | --------- | ------- |
| title | CharField | VARCHAR |
| slug  | SlugField | VARCHAR |
| body  | TextField | TEXT    |
| id    | AutoField | INT PK  |

---

## Vistas (`views.py`) y URLs

* **post\_list:** lista posts publicados.
* **post\_detail:** detalle de post por ID (si está publicado).
* URLs de la app `blog/urls.py` → define rutas con namespace.
* `mysite/urls.py` → incluye rutas principales y conecta app `blog`.

> Ver código para ejemplos y comentarios de cada función.

---

## Admin de Django (`admin.py`)

* Configura filtros, búsqueda, prepopulated fields, orden y jerarquía por fecha.
* Permite gestionar posts y usuarios desde interfaz web.

---

## Templates (resumen)

* `base.html` → plantilla base con bloques (`title`, `content`) y sidebar.
* `list.html` → lista de posts con título, fecha, autor y resumen.
* `detail.html` → detalle de post con contenido completo.

> Ver HTML para comentarios y estructura detallada.

---

## Conceptos clave

* **Manager personalizado:** `Post.published.all()`.
* **Meta:** orden descendente e índices para optimizar consultas.
* **Request/Response cycle:** navegador → Django → view → template → HTML.
* **Admin:** gestiona posts y usuarios.

---

## Archivos `.py` usados

* `mysite/settings.py` → configuración general del proyecto
* `mysite/urls.py` → rutas principales
* `blog/models.py` → modelo Post + manager `published`
* `blog/views.py` → vistas de la app
* `blog/admin.py` → admin
* `blog/urls.py` → rutas de la app

> El resto de archivos generados (`apps.py`, `tests.py`, `migrations/`) son soporte o para futuras pruebas/migraciones.

---

---

# Proyecto Blog Mejorado - Django 4 (Capítulo 2)

## Resumen del proyecto

* Este proyecto continúa sobre el Blog del Capítulo 1, agregando funcionalidades más avanzadas y mejorando la estructura de código.
* Temas principales del Capítulo 2:

  * **URLs canónicas y amigables para SEO** con `get_absolute_url` y `slug`.
  * **Paginación** de posts largos.
  * **Class-Based Views (CBV)** para reemplazar views basadas en funciones (FBV).
  * **Formularios y envío de email** con `EmailPostForm`.
  * **Sistema de comentarios** con `CommentForm`.
  * **Templates reutilizables** y mensajes de éxito.
* Se mantiene el patrón **MTV (Model-Template-View)** de Django:

  * **Model:** maneja datos y la base de datos.
  * **Template:** define la presentación y diseño visual.
  * **View:** controla la lógica y la interacción con el usuario.
* Filosofía **DRY (Don't Repeat Yourself):** reutilización de código y desarrollo rápido.

---

## Canonical URLs y SEO

* Cada `Post` tiene un **slug**, que es una versión amigable del título (sin espacios, acentos ni caracteres especiales) para usar en la URL.
* Método **`get_absolute_url`** en el modelo `Post`:

```python
from django.urls import reverse

class Post(models.Model):
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    
    def get_absolute_url(self):
        # Devuelve la URL canónica del post
        return reverse('blog:post_detail', args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug
        ])
```

> Esto permite que los posts tengan **URLs limpias y fáciles de leer**, además de ser **optimizado para SEO**.

---

## Paginación de posts

* Cuando tenemos muchos posts, Django ofrece un **paginador** para dividir la lista en páginas:

```python
from django.core.paginator import Paginator

paginator = Paginator(object_list, 3)  # 3 posts por página
page_number = request.GET.get('page', 1)  # número de página desde la URL
page_obj = paginator.get_page(page_number)  # objetos de la página actual
```

* En el template HTML:

```html
{% if page_obj.has_previous %}
<a href="?page={{ page_obj.previous_page_number }}">Anterior</a>
{% endif %}

{% if page_obj.has_next %}
<a href="?page={{ page_obj.next_page_number }}">Siguiente</a>
{% endif %}
```

> Esto **mejora la experiencia de usuario** y evita cargar todos los posts a la vez.

---

## Class-Based Views (CBV)

* Las CBV **reemplazan las views basadas en funciones (FBV)** y permiten reducir código repetido.
* Ejemplo de lista de posts publicados:

```python
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    queryset = Post.published.all()  # posts publicados
    context_object_name = 'posts'    # variable disponible en template
    paginate_by = 3                  # posts por página
    template_name = 'blog/post/list.html'  # template usado
```

* Ventajas:

  * **Reutilización de código.**
  * Integración automática con **paginación** y **templates**.
  * Fácil de extender con filtros o lógica adicional.

---

## Formularios y envío de email

### Formulario `EmailPostForm`

```python
from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)           # nombre del remitente
    email = forms.EmailField()                      # email del remitente
    to = forms.EmailField()                         # email del destinatario
    comments = forms.CharField(required=False, widget=forms.Textarea)  # comentario opcional
```

### Configuración de email en `settings.py`

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'tu_email@gmail.com'
EMAIL_HOST_PASSWORD = 'tu_app_password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

* Se recomienda usar **App Password** para Gmail y evitar exponer tu contraseña.

### Vista para compartir posts

```python
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recomienda {post.title}"
            message = f"Lee {post.title} en {post_url}\n\nComentario de {cd['name']}: {cd['comments']}"
            send_mail(subject, message, 'tu_email@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()

    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})
```

---

## Sistema de comentarios

### Modelo `Comment`

```python
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']  # comentarios ordenados por fecha
```

### Formulario `CommentForm`

```python
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
```

### Vista para procesar comentarios

```python
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, render

@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comment = None
    form = CommentForm(data=request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

    return render(request, 'blog/post/comment.html', {'post': post, 'form': form, 'comment': comment})
```

* En `post_detail.html`, se incluyen los comentarios activos y el formulario:

```django
{% include "blog/post/includes/comment_form.html" %}
```

---

## URLs de la app `blog/urls.py`

```python
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
]
```

> URLs amigables con fecha y slug, optimizadas para SEO.

---

## Templates principales

* `base.html` → plantilla base con bloques `title` y `content`.
* `list.html` → lista de posts con **paginación**.
* `detail.html` → detalle de post con **comentarios** y enlace para compartir.
* `share.html` → formulario de **enviar por email**.
* `comment.html` → formulario de **comentario** y mensaje de éxito.
* `includes/comment_form.html` → template reutilizable para formulario de comentarios.

---

## Flujo de trabajo aplicado

1. **Forms (`forms.py`)** → definir qué datos necesitamos del usuario.
2. **Settings (`settings.py`)** → configurar SMTP u otros ajustes necesarios.
3. **Views (`views.py`)** → lógica de procesamiento de formularios, comentarios y paginación.
4. **URLs (`urls.py`)** → conectar vistas con rutas amigables.
5. **Templates (`.html`)** → presentación final, mensajes y bloques reutilizables.

```
Forms  →  Settings  →  Views  →  URLs  →  Templates
```

> Este flujo refleja la recomendación del libro: primero definir **qué queremos hacer**, luego asegurar que el **entorno está listo**, después implementar **la lógica**, conectar con **URLs** y finalmente presentar la información al usuario en **templates**.

---

