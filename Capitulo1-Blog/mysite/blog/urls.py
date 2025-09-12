from django.urls import path
from . import views

app_name = 'blog'  # namespace de la app

urlpatterns = [
    path('', views.post_list, name='post_list'),        # lista de posts
    path('<int:id>/', views.post_detail, name='post_detail'),  # detalle por ID
]
