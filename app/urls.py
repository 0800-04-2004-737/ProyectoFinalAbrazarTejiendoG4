from django.urls import path
from abrazartejiendo import urls
from app import views

urlpatterns = [
    path('', views.Menu),
    path('index.html/', views.Menu, name = 'index'),
]