# Generated by Django 4.2.1 on 2024-11-16 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentapp', '0009_remove_userdador_tipo_remove_usertario_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdador',
            name='tipo',
            field=models.CharField(max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='usertario',
            name='tipo',
            field=models.CharField(max_length=24, null=True),
        ),
    ]