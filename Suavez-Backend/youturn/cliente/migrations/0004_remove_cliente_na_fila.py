# Generated by Django 4.1.5 on 2024-02-09 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_cliente_na_fila'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='na_fila',
        ),
    ]