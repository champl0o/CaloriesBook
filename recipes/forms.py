from django import forms
from .models import Recipe, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
