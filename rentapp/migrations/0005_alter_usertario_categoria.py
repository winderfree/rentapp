# Generated by Django 4.2.1 on 2023-11-29 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentapp', '0004_amistad_renta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertario',
            name='categoria',
            field=models.CharField(choices=[('propietario', 'Propietario'), ('abogado', 'Abogado'), ('empresa', 'Empresa o Compañia')], max_length=24),
        ),
    ]