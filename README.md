# 📓 Apuntes Django - Proyecto Blog

Voy anotando lo esencial de cada capítulo.  
Nada muy largo, solo lo que me sirva de recordatorio rápido.

---

## ✨ Capítulo 1 – Blog

### 🛠️ Setup rápido
- Crear entorno virtual → `python3 -m venv venv`  
- Activar (Linux/Mac) → `source venv/bin/activate`  
- Activar (Windows) → `venv\Scripts\activate`  
- Instalar Django → `pip install django==4.1.0`  
- Verificar versión → `python3 -m django --version`  
- Instalar dependencias → `pip install -r requirements.txt`  

### 🧩 Arquitectura MTV (Model - Template - View)
- **Model** → maneja la BD.  
- **Template** → presentación (HTML, lo que ve el usuario).  
- **View** → lógica que conecta Model con Template.  
- **Controller** → lo maneja Django internamente (URLs → View).  

📌 Filosofía Django → **DRY (Don't Repeat Yourself)**.  

### 🚀 Novedades Django 4
- Caching con Redis.  
- Scrypt password hasher.  
- Formularios con templates.  
- Soporte ASGI + ORM asíncrono.  

---

## 🔜 Capítulo 2
*(pendiente)*  
