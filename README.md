# 📓 Apuntes Django - Proyecto Blog

Este documento guarda mis notas del Capítulo 1 del libro *Django 4 by Example*.
Se centra en setup, arquitectura y estructura inicial del proyecto.

---

## ✨ Capítulo 1 – Blog

### 🛠️ Setup rápido

* Crear entorno virtual:

  ```bash
  python3 -m venv venv
  ```
* Activar entorno:

  * Linux/Mac → `source venv/bin/activate`
  * Windows → `venv\Scripts\activate`
* Instalar Django: `pip install django==4.1.0`
* Verificar versión: `python3 -m django --version`
* Instalar dependencias: `pip install -r requirements.txt`

---

### 🧩 Arquitectura MTV (Model - Template - View)

* **Model** → maneja la base de datos.
* **Template** → presentación (HTML, lo que ve el usuario).
* **View** → lógica que conecta Model con Template.
* **Controller (implícito)** → Django enruta URLs a Views.

📌 Filosofía Django → **DRY (Don’t Repeat Yourself)**.

---

### 🔄 Ciclo petición/respuesta

1. Navegador pide una **URL**.
2. Django busca en **URL patterns** y ejecuta la **View** correspondiente.
3. La **View** consulta los **Modelos** si hace falta.
4. Renderiza un **Template** (HTML) y devuelve **HTTP response**.

* Extra: **Middleware** = código que intercepta/modifica este flujo (ej: seguridad, sesiones).

---

### 📂 Estructura del proyecto Django

```
Capitulo1-Blog/
  mysite/
    manage.py        # utilidad CLI, no se edita
    mysite/
      __init__.py    # marca el directorio como paquete Python
      asgi.py        # configuración ASGI (async server)
      settings.py    # configuración global del proyecto
      urls.py        # rutas principales
      wsgi.py        # configuración WSGI (sync server)
  requirements.txt
```

* `settings.py` contiene `DATABASES` y `INSTALLED_APPS`.
* Base de datos por defecto: **SQLite3** (ligera, para desarrollo).
* Para producción → PostgreSQL / MySQL / Oracle.

---

### ⚡ Novedades Django 4 que se pueden aprovechar

* **Caching con Redis**
* **Scrypt password hasher**
* **Renderizado de formularios con templates**
* **Soporte ASGI y ORM asíncrono**

---

### ✅ Migraciones iniciales

* Aplicar tablas de apps por defecto (admin, auth, sessions, etc.):

```bash
cd mysite        # carpeta que contiene manage.py
python manage.py migrate
```

* Levantar servidor:

```bash
python manage.py runserver
```

* URL de desarrollo: `http://127.0.0.1:8000/`

---

### 🔹 Verificar servidor de desarrollo y entornos

* Abrir en el navegador:

  ```
  http://127.0.0.1:8000/
  ```

  * Deberías ver la **página por defecto de Django** indicando que el proyecto corre correctamente.
  * Cada solicitud HTTP se registra en la consola, ejemplo:

    ```
    [01/Jan/2022 17:20:30] "GET / HTTP/1.1" 200 16351
    ```

* Ejecutar servidor con host/puerto y settings específicos:

```bash
python manage.py runserver 127.0.0.1:8001 --settings=mysite.settings
```

* Útil para distintos entornos (desarrollo, staging, etc.)

* ⚠️ Nota de producción:

  * `runserver` **solo es para desarrollo**, no para producción.
  * Para producción usar:

    * **WSGI** → Apache, Gunicorn, uWSGI
    * **ASGI** → Daphne, Uvicorn

---

### 📝 Mini nota para apuntes / README Cap 1

* Ejecutar **manage.py** desde la carpeta correcta.
* Revisar **migraciones pendientes**: `python manage.py migrate`.
* Carpeta raíz del proyecto = contiene `manage.py`.
* Carpeta `mysite/` dentro del proyecto = paquete Python con configuración (settings, urls, asgi/wsgi).
* URLs activas por defecto:

  * /admin/ → panel de administración
  * /blog/ → app del blog
* Cambiar host/puerto o settings:
  python manage.py runserver 127.0.0.1:8001 --settings=mysite.settings
* Servidor dev solo para pruebas; producción: usar WSGI o ASGI.
