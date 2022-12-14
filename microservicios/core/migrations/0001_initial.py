# Generated by Django 4.1.2 on 2022-10-04 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(help_text='Nombre del cliente', max_length=250)),
                ('correo_electronico', models.EmailField(max_length=250)),
                ('telefono_contacto', models.CharField(default='', max_length=9)),
            ],
        ),
    ]
