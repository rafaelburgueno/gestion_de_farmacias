# Generated by Django 3.2.8 on 2021-11-02 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionUsuarios', '0007_auto_20211023_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='rol',
            field=models.ForeignKey(default='usuario', on_delete=django.db.models.deletion.CASCADE, to='gestionUsuarios.roles'),
        ),
    ]