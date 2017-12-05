from django.db import models


class Factura(models.Model):
    nombre = models.CharField(max_length=20, null=False)
    monto = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    monto_letras = models.CharField(max_length=100, null=False)
