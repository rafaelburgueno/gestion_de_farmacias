# Generated by Django 3.2 on 2021-12-01 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionStock', '0003_alter_lotes_vencimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lotes',
            name='vencimiento',
            field=models.DateTimeField(blank=True, max_length=50, null=True, verbose_name='Fecha de vencimiento'),
        ),
    ]
