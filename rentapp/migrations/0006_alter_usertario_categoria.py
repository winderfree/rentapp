# Generated by Django 4.2.1 on 2023-11-30 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentapp', '0005_alter_usertario_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertario',
            name='categoria',
            field=models.CharField(max_length=24),
        ),
    ]
