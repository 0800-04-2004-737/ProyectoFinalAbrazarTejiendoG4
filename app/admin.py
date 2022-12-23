from django.contrib import admin
from .models import Post

# Register your models here.

# ejemplo:
# from django.contrib import admin
# from app import models

# admin.site.register(models.Tabla_test, admin.ModelAdmin)
# admin.site.register(models.Project, admin.ModelAdmin)

admin.site.register(Post)
