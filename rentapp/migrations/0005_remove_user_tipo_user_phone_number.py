# Generated by Django 4.2.1 on 2025-01-12 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentapp', '0004_alter_user_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tipo',
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Número Celular'),
        ),
    ]
