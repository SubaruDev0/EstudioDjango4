from django import forms
from.models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)          # Nombre del remitente
    email = forms.EmailField()                     # Correo del remitente
    to = forms.EmailField()                        # Correo del destinatario
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea                       # Comentarios opcionales en <textarea>
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']
