# Generated by Django 3.2.8 on 2021-11-25 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestionStock', '0003_lotes_funcionario'),
    ]

    operations = [
        migrations.AddField(
            model_name='lotes',
            name='destinatario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destinatario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lotes',
            name='funcionario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='funcionario', to=settings.AUTH_USER_MODEL),
        ),
    ]