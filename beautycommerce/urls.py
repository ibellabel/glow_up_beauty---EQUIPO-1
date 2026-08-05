from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from core.views import CrearOrdenView


def inicio(request):
    return HttpResponse("""
    <h1>Beauty Commerce</h1>
    <p> El servidor de Django está funcionando correctamente.</p>

    <h2>Rutas disponibles</h2>
    <ul>
        <li><a href="/admin/">Panel de administración</a></li>
        <li><a href="/api/ordenes/crear/">Crear orden</a></li>
    </ul>
    """)


urlpatterns = [
    path("", inicio, name="inicio"),
    path("admin/", admin.site.urls),
    path("api/ordenes/crear/", CrearOrdenView.as_view(), name="crear_orden"),
]