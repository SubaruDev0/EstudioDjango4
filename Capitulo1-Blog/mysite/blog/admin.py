from django.contrib import admin
from .models import Post

# Registrar modelo Post en admin con opciones de visualización

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status'] # columnas
    list_filter = ['status', 'created', 'publish', 'author'] # filtros
    search_fields = ['title', 'body'] # búsqueda
    prepopulated_fields = {'slug': ('title',)} # autocompletar slug
    raw_id_fields = ['author'] # optimiza selects
    date_hierarchy = 'publish' # jerarquía fechas
    ordering = ['status', 'publish'] # orden por defecto