from django.contrib import admin
from .models import Marca, Usuario, Producto, Orden

admin.site.register(Marca)
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Orden)