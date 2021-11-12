# Generated by Django 3.2.8 on 2021-11-09 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmacias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('localidad', models.CharField(blank=True, max_length=100, null=True)),
                ('departamento', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Farmacia',
                'verbose_name_plural': 'Farmacias',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Medicamentos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_comercial', models.CharField(max_length=100)),
                ('categoria', models.CharField(blank=True, choices=[('VL', 'Venta Libre'), ('RV', 'Receta Verde'), ('FNR', 'Fondo Nacional De Recursos')], max_length=50, null=True, verbose_name='Categoria(venta libre, receta verde o FNR)')),
                ('laboratorio', models.CharField(blank=True, max_length=100, null=True)),
                ('principio_activo', models.CharField(blank=True, max_length=200, null=True)),
                ('forma', models.CharField(blank=True, max_length=50, null=True)),
                ('contraindicaciones', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'Medicamento',
                'verbose_name_plural': 'Medicamentos',
                'ordering': ['nombre_comercial'],
            },
        ),
        migrations.CreateModel(
            name='Lotes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stock', models.IntegerField()),
                ('ingreso', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de ingreso')),
                ('vencimiento', models.CharField(blank=True, max_length=50, null=True, verbose_name='Fecha de vencimiento')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de edición')),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionStock.medicamentos')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionStock.farmacias')),
            ],
            options={
                'verbose_name': 'Lote',
                'verbose_name_plural': 'Lotes',
                'ordering': ['stock'],
            },
        ),
    ]