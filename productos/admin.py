from django.contrib import admin
from .models import categoria, productos, clientes, venta, Detalleventa

admin.site.register(categoria)
admin.site.register(productos)
admin.site.register(clientes)
admin.site.register(venta)
admin.site.register(Detalleventa)