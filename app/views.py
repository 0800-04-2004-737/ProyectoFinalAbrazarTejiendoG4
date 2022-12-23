from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, PostEdit
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.db import IntegrityError
# from django.http import HttpResponse

# Create your views here.
# def Menu(request):
#     return render(request, 'index.html')

# def Nosotros(request):
#     return render(request, 'nosotros.html')

# def Info(request):
#     return render(request, 'informacion.html')

# def Prueba(request):
#     return render(request, 'prueba.html')

# def index(request):
#     return render(request, 'index.html')


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

# Header


class HomeView(ListView):
    model = Post
    template_name = 'index.html'

class HomeView1(ListView):
    model = Post
    template_name = 'comentarios.html'

class About(ListView):
    model = Post
    template_name = 'nosotros.html'


class News(ListView):
    model = Post
    template_name = 'anuncios.html'


class Contact(ListView):
    model = Post
    template_name = 'contacto.html'


class LoginView(ListView):
    model = Post
    template_name = 'login.html'


class Commentary(CreateView):
    model = Post
    template_name = 'add_post.html'
    # fields = '__all__'
    form_class = PostForm

class UpdatePost(UpdateView):
    model = Post
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']
    form_class = PostEdit

# def Sesion(request):
#     if request.method == 'GET':
#         return render(request, 'pruebalogin.html',{
#         'form' : UserCreationForm
#     })
    

def login(request):
    
    if request.method == 'GET':
        return render(request, 'pruebalogin.html',{
        'form' : UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            #registrar usuario
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('home')
            except IntegrityError:
                return render(request, 'pruebalogin.html',{
                'form' : UserCreationForm,
                'error' : 'El usuario ya existe'
                })

        return render(request, 'pruebalogin.html',{
                'form' : UserCreationForm,
                'error' : 'La contraseña es incorrecta'
                })

def singout(request):
    auth_logout(request)
    return redirect('home')

def singin(request):
    if request.method == 'GET':
        return render(request, 'singin.html', {
        'form' : AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'singin.html', {
            'form' : AuthenticationForm,
            'error' : 'El usuario o contraseña es incorrecta'
        })
        else:
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
