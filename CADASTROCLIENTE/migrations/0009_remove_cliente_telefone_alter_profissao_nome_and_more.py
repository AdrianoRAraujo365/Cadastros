# Generated by Django 4.2 on 2023-04-25 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CADASTROCLIENTE', '0008_alter_cliente_options_alter_profissao_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='telefone',
        ),
        migrations.AlterField(
            model_name='profissao',
            name='nome',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ddd', models.CharField(max_length=3)),
                ('numero', models.CharField(max_length=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CADASTROCLIENTE.cliente')),
            ],
        ),
    ]