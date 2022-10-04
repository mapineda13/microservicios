from django.db import models

# Create your models here.
class ClienteModel(models.Model):
    nombre_completo = models.CharField(
        max_length=250,
        help_text='Nombre del cliente'
    )
    correo_electronico = models.EmailField(
        max_length=250
    )
    telefono_contacto = models.CharField(
        max_length=9,
        default=""
    )