from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse  # para generar URLs amigables

# Manager personalizado → solo posts publicados
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post(models.Model):
    # Estado del post
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)  # título del post
    slug = models.SlugField(max_length=250, unique_for_date='publish')  # URL amigable única por fecha
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()  # contenido del post
    publish = models.DateTimeField(default=timezone.now)  # fecha de publicación
    created = models.DateTimeField(auto_now_add=True)  # fecha de creación
    updated = models.DateTimeField(auto_now=True)  # fecha de actualización
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    # Managers
    objects = models.Manager()  # manager por defecto
    published = PublishedManager()  # manager personalizado

    class Meta:
        ordering = ['-publish']  # orden descendente
        indexes = [
            models.Index(fields=['-publish']),  # índice en publish
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Retorna la URL canónica del post.
        Usa el nombre de la URL 'blog:post_detail' y los argumentos
        año, mes, día y slug para generar un enlace único.
        """
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

class Comment(models.Model):
    # Relación 1:N → un post tiene muchos comentarios
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),  # índice en created
        ]

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
