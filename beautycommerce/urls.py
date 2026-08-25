from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from core.views import CrearOrdenView
from tienda.views import (
    ProductoListView,
    CategoriaListView,
    ResenaListCreateView,
    DireccionEnvioListCreateView,
)


def inicio(request):
    return HttpResponse("""
    <h1>Beauty Commerce</h1>
    <p> El servidor de Django está funcionando correctamente.</p>

    <h2>Rutas disponibles</h2>
    <ul>
        <li><a href="/admin/">Panel de administración</a></li>
        <li><a href="/api/productos/">Listar productos (GET)</a></li>
        <li><a href="/api/categorias/">Listar categorías (GET)</a></li>
        <li><a href="/api/resenas/">Listar/crear reseñas (GET/POST)</a></li>
        <li><a href="/api/direcciones/">Listar/crear direcciones (GET/POST)</a></li>
        <li>Crear orden: POST /api/ordenes/crear/</li>
    </ul>
    """)


urlpatterns = [
    path("", inicio, name="inicio"),
    path("admin/", admin.site.urls),
    path("api/ordenes/crear/", CrearOrdenView.as_view(), name="crear_orden"),
    path("api/productos/", ProductoListView.as_view(), name="listar_productos"),
    path("api/categorias/", CategoriaListView.as_view(), name="listar_categorias"),
    path("api/resenas/", ResenaListCreateView.as_view(), name="resenas"),
    path("api/direcciones/", DireccionEnvioListCreateView.as_view(), name="direcciones"),
]