"""Facturacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from facturacion.utils.generar_documentos import crear_recibo
from facturacion.views import FacturaFormView, LoginFormView, LogoutView, RootRedirectView, FacturaListView, \
    FacturaDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RootRedirectView.as_view(), name='root'),
    path('nueva-factura', FacturaFormView.as_view(), name='crear-factura'),
    path('factura/list', FacturaListView.as_view(), name='lista-factura'),
    path('factura/ver-factura/<int:pk>/', FacturaDetailView.as_view(), name='detalle-factura'),
    path('factura/generar-pdf/<int:pk>/', crear_recibo, name='crear-pdf-factura'),
    path('login/', LoginFormView.as_view(), name='iniciar-sesion'),
    path('logout/', LogoutView.as_view(), name='cerrar-sesion'),
]
