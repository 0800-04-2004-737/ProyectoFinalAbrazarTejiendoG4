# Generated by Django 4.1.4 on 2022-12-22 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_noticia_imagen_alter_post_title_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentarios',
            old_name='cuerpo_comentario',
            new_name='comentario',
        ),
    ]
