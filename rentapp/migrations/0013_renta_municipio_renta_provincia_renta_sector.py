# Generated by Django 4.2.1 on 2023-10-07 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentapp', '0012_alter_renta_latitud_alter_renta_longitud'),
    ]

    operations = [
        migrations.AddField(
            model_name='renta',
            name='municipio',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='renta',
            name='provincia',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='renta',
            name='sector',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
