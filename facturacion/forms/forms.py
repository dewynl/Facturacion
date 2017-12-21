from django.forms import ModelForm

from facturacion.models import Factura


class FacturaForm(ModelForm):
    class Meta:
        model = Factura
        fields = ['nombre', 'monto', 'concepto']