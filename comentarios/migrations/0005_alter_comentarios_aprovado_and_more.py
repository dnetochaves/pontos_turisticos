# Generated by Django 4.0.4 on 2022-07-24 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comentarios', '0004_remove_comentarios_teste'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='aprovado',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='comentario',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='data',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]