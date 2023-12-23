# Generated by Django 4.0.6 on 2023-12-21 22:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('panel_principal', '0002_rename_post_author_id_posteos_usuarios_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteos_usuarios',
            name='post_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
