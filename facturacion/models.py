from django.db import models


class Factura(models.Model):
    fecha = models.DateField(auto_now=True)
    nombre = models.CharField(max_length=30, null=False)
    monto = models.IntegerField(default=0)
    monto_palabras = models.CharField(max_length=100, null=False, blank=True)
    concepto = models.TextField(max_length=130, null=True)
