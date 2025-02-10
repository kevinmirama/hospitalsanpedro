from django.db import models


class Universidad(models.Model):
    nombre = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    email = models.EmailField()


class Documento(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Aprobado', 'Aprobado'),
        ('Rechazado', 'Rechazado'),
    ]
    universidad = models.ForeignKey(Universidad, on_delete=models.CASCADE)
    nombre_archivo = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='documentos/')
    fecha_subida = models.DateTimeField(auto_now_add=True)
    estado_aprobacion = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default='Pendiente'
    )
