# Generated by Django 4.0.6 on 2023-12-21 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel_principal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posteos_usuarios',
            old_name='post_author_id',
            new_name='post_author',
        ),
    ]
