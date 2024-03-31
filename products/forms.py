from django.forms import ModelForm, Textarea

from .models import Comment

class CommentsForm(ModelForm):
    
    class Meta:
        model = Comment
        fields = ("text",) 
        
        # Para hacer mas bonito el formulario en el template, podemos añadir elementos adicionales.
        widgets = {
            "text":Textarea(attrs={
                "class": "form-control",
                "aria-label": "Comentarios",
                "placeholder": "Deja tu comentario",
                "id": "formComment"
            })
        }