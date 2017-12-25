import time

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from django.views.generic import FormView, RedirectView, ListView

from facturacion.forms.forms import FacturaForm, LoginForm
from facturacion.models import Factura
from facturacion.utils.generar_documentos import crear_recibo
from facturacion.utils.number_to_letter import to_word


class RootRedirectView(RedirectView):
    pattern_name = 'crear-factura'


class LogoutView(RedirectView):
    pattern_name = 'iniciar-sesion'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class LoginFormView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/nueva-factura'

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user:
            login(self.request, user=user)

        return super(LoginFormView, self).form_valid(form)


class FacturaFormView(LoginRequiredMixin, FormView):
    template_name = 'crear-factura.html'
    form_class = FacturaForm
    login_url = '/login'
    success_url = '/nueva-factura'

    def form_valid(self, form):
        factura = Factura(nombre=form.cleaned_data['nombre'], monto=int(form.cleaned_data['monto']),
                          concepto=form.cleaned_data['concepto'])
        factura.monto_palabras = to_word(factura.monto)
        factura.monto_palabras = factura.monto_palabras + " Pesos Dominicanos."
        factura.fecha = time.strftime("%d/%m/%Y")
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="factura.pdf"'
        pdf = crear_recibo(factura)
        response.write(pdf)
        factura.save()
        return response


class FacturaListView(ListView):
    model = Factura
    template_name = 'facturas_list.html'
    queryset = Factura.objects.all().order_by('id')

