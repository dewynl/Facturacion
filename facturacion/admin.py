from django.contrib import admin

from facturacion.models import Factura


class FacturaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'monto', 'concepto')


admin.site.register(Factura, FacturaAdmin)
