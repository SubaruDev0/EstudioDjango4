from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),                # admin
    path('blog/', include('blog.urls', namespace='blog')),  # URLs de blog
]
