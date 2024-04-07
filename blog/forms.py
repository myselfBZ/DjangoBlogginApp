from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.utils import ErrorList
from .models import Post, Comment

class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['title'].widget.attrs['class'] = 'form-control form-control-lg'
    class Meta:
        model = Post
        fields = ['title', 'content']
    
class CommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['class'] = 'form-control form-control-lg'
    class Meta:
        model = Comment
        fields = ['content']