# Generated by Django 4.0.5 on 2022-07-30 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('sub_titulo', models.CharField(max_length=250)),
                ('contenido', models.CharField(max_length=500)),
                ('autor', models.CharField(max_length=500)),
                ('fecha_creacion', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagenes', models.ImageField(blank=True, null=True, upload_to='iamgenes')),
            ],
        ),
    ]
