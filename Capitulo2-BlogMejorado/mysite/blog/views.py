from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST

# Detalle del post
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    comments = post.comments.filter(active=True)  # <-- CORREGIDO
    form = CommentForm()
    return render(request, 'blog/post/detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })


# Lista de posts (CBV)
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'blog/post/list.html'

# Compartir post por email
def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} te recomienda leer {post.title}"
            message = f"Lee {post.title} en {post_url}\n\n" \
                      f"{cd['name']} comenta: {cd['comments']}"
            send_mail(subject, message, 'subaruzerokara@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()

    return render(request, 'blog/post/share.html', {
        'post': post,
        'form': form,
        'sent': sent
    })

# Crear comentario
@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    comment_submitted = False  # Flag para indicar que se envió

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        comment_submitted = True  # Comentario guardado

    return render(request, 'blog/post/comment.html', {
        'post': post,
        'form': form,
        'comment': comment,
        'comment_submitted': comment_submitted
    })
