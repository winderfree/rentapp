# Generated by Django 4.2.1 on 2024-11-16 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentapp', '0006_alter_usertario_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdador',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='usertario',
            name='tipo',
        ),
    ]