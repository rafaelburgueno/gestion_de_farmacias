# Generated by Django 3.2.8 on 2021-10-21 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionUsuarios', '0002_alter_recetas_paciente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
