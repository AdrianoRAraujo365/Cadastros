# Generated by Django 4.2 on 2023-04-24 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CADASTROCLIENTE', '0004_remove_cliente_estadp_civil_cliente_estado_civil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=120, unique=True),
        ),
    ]
