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
- Instalación de dependencias:
  ```bash
  pip install -r requirements.txt
