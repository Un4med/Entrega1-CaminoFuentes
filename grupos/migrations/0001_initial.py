# Generated by Django 4.0.5 on 2022-07-23 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dios', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('fecha_creacion', models.DateField(null=True)),
            ],
        ),
    ]