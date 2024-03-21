# Generated by Django 5.0.2 on 2024-03-21 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buzo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articulo', models.CharField(max_length=50, null=True)),
                ('categoria', models.CharField(max_length=50, null=True)),
                ('descripcion', models.CharField(max_length=100, null=True)),
                ('talle', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pantalon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articulo', models.CharField(max_length=50, null=True)),
                ('categoria', models.CharField(max_length=50, null=True)),
                ('modelo', models.CharField(max_length=50, null=True)),
                ('talle', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Remera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articulo', models.CharField(max_length=50, null=True)),
                ('categoria', models.CharField(max_length=50, null=True)),
                ('modelo', models.CharField(max_length=50, null=True)),
                ('talle', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('dni', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('cuentaDePago', models.CharField(max_length=50)),
            ],
        ),
    ]
