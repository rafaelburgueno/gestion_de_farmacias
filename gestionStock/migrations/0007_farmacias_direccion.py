# Generated by Django 3.2.8 on 2021-10-14 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionStock', '0006_auto_20211014_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmacias',
            name='direccion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
