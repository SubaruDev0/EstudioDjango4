# 📓 Apuntes de *Django for APIs*

Voy guardando mis notas capítulo por capítulo.  
No son explicaciones largas, solo lo esencial que necesito recordar.

---

## ✨ Capítulo 1 – Blog con Django

- Django = framework Python → rápido, seguro, pensado para proyectos grandes.  
- Usaremos **DRF** (Django REST Framework) más adelante para APIs.  

### 🔧 Setup
- Crear entorno virtual → `python -m venv .venv`  
- Activar y `pip install django`  
- Crear proyecto → `django-admin startproject config .`  
- Crear app → `python manage.py startapp posts`

### 📂 Estructura
- `config/` → settings, urls, etc.  
- `posts/` → nuestra app de blog.  

### 📝 Modelo
```python
class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
