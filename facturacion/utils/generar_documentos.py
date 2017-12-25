import io

from django.http import HttpResponse
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

from facturacion.models import Factura


def crear_recibo(request, pk):
    factura = Factura.objects.filter(pk=pk).first()
    buffer = io.BytesIO()
    # TAMANO_HOJA = (9.0 * inch, 5.5 * inch)
    TAMANO_HOJA = (9.5 * inch, 11 * inch)
    altura = 11 * inch
    can = canvas.Canvas(buffer, pagesize=TAMANO_HOJA)

    # Header
    can.setLineWidth(.4)
    can.setFont('Helvetica-Bold', 12)
    can.drawString(0.5 * inch, altura - 0.5 * inch, 'INVERSIONES LIRIANO')
    can.setFont('Helvetica', 14)
    can.drawString(8.0 * inch, altura - 0.5 * inch, str(factura.fecha))
    can.setFont('Helvetica', 8)
    can.drawString(0.5 * inch, altura - 0.6 * inch, 'C/ GENEROSO DIAS #7 MOD 2 DETRÁS DE BAUTISTA MOTOR.')
    can.drawString(0.5 * inch, altura - 0.7 * inch, 'SANTIAGO, REP. DOM.')
    can.drawString(0.5 * inch, altura - 0.8 * inch, 'Teléfonos: 809-276-3555 / 829-902-1118')
    can.setFont('Helvetica-Bold', 14)
    can.drawString(3.75 * inch, altura - 1.1 * inch, 'RECIBO DE INGRESOS')
    can.line(0.5 * inch, altura - 1.2 * inch, 9.5 * inch, altura - 1.2 * inch)
    can.setFont('Helvetica', 12)
    can.drawString(0.5 * inch, altura - 1.5 * inch, 'HEMOS RECIBIDO DE:')
    can.line(2.4 * inch, altura - 1.6 * inch, 8.5 * inch, altura - 1.6 * inch)
    can.setFont('Helvetica-Bold', 12)
    can.drawString(2.90 * inch, altura - 1.5 * inch, factura.nombre)
    can.setFont('Helvetica', 12)
    can.drawString(0.5 * inch, altura - 1.9 * inch, "LA SUMA DE:")
    can.setFont('Helvetica-Bold', 14)
    can.line(1.7 * inch, altura - 1.9 * inch, 8.5 * inch, altura - 1.9 * inch)
    can.drawString(2.3 * inch, altura - 1.85 * inch, "RD$ " + str(factura.monto))
    can.line(1.7 * inch, altura - 2.3 * inch, 8.5 * inch, altura - 2.3 * inch)
    can.drawString(2.3 * inch, altura - 2.2 * inch, str(factura.monto_palabras))

    can.setFont('Helvetica', 12)
    can.drawString(0.5 * inch, altura - 2.6 * inch, "CONCEPTO:")
    can.setFont('Helvetica-Bold', 12)
    can.line(1.5 * inch, altura - 2.6 * inch, 8.5 * inch, altura - 2.6 * inch)
    can.line(0.5 * inch, altura - 3 * inch, 8.5 * inch, altura - 3 * inch)

    if len(factura.concepto) < 70:
        can.drawString(2.0 * inch, altura - 2.55 * inch, factura.concepto)
    else:
        can.drawString(1.8 * inch, altura - 2.55 * inch, factura.concepto[:70] + "-")
        can.drawString(0.7 * inch, altura - 2.95 * inch, factura.concepto[70:])
    can.setFont('Helvetica', 12)
    can.line(6.5 * inch, altura - 3.4 * inch, 8.5 * inch, altura - 3.4 * inch)
    can.drawString(7.0 * inch, altura - 3.4 * inch, "Firma y Sello")
    can.showPage()
    can.save()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="factura.pdf"'
    pdf = buffer.getvalue()
    response.write(pdf)
    return response
