# Generated by Django 4.2.1 on 2023-09-27 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentapp', '0006_amistad_mensaje_userdador_usertario_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='renta',
            name='e_mail',
        ),
        migrations.RemoveField(
            model_name='renta',
            name='telefono',
        ),
    ]