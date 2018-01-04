from django.forms import ModelForm
from django import forms

from facturacion.models import Factura


class FacturaForm(ModelForm):
    class Meta:
        model = Factura
        fields = ['nombre', 'monto', 'concepto']

    def __init__(self, *args, **kwargs):
        super(FacturaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class LoginForm(forms.Form):
    username = forms.CharField(max_length=15, min_length=5)
    password = forms.CharField(widget=forms.PasswordInput())
