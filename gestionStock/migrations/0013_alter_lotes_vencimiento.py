# Generated by Django 3.2.8 on 2021-11-05 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionStock', '0012_alter_lotes_vencimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lotes',
            name='vencimiento',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Fecha de vencimiento'),
        ),
    ]
