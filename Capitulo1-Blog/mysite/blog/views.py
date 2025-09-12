from django.shortcuts import render, get_object_or_404
from .models import Post

# Lista de posts
def post_list(request):
    posts = Post.published.all()  # solo posts publicados
    return render(request, 'blog/post/list.html', {'posts': posts})

# Detalle de un post
def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)  # 404 si no existe
    return render(request, 'blog/post/detail.html', {'post': post})
