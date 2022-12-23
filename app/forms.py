from django import forms
from .models import Post

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'title_tag', 'author', 'body']

    widgets = {
      'title': forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Escriba el titulo'}),
      'title_tag': forms.TextInput(attrs = {'class' : 'form-control'}),
      'author': forms.TextInput(attrs = {'class' : 'form-control', 'value' : '', 'id' : 'user_id', 'type' : 'hidden'}),
      'body': forms.Textarea(attrs = {'class' : 'form-control'}),
    }

class PostEdit(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'title_tag', 'body']

    widgets = {
      'title': forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Escriba el titulo'}),
      'title_tag': forms.TextInput(attrs = {'class' : 'form-control'}),
      'author': forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Usuario', 'id' : 'user_id'}),
      'body': forms.Textarea(attrs = {'class' : 'form-control'}),
    }