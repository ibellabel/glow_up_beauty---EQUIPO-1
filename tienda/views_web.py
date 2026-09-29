from django.shortcuts import render
from django.db.models import Avg, Count, Case, When, IntegerField

from tienda.models import Categoria, Producto


def home(request):
    categorias = Categoria.objects.all()
    panels = []
    for categoria in categorias:
        productos = (
            Producto.objects.filter(categoria=categoria)
            .annotate(
                rating_promedio=Avg("resenas__calificacion"),
                total_resenas=Count("resenas"),
                resenas_creadoras=Count(
                    Case(When(resenas__es_creadora=True, then=1), output_field=IntegerField())
                ),
            )
            .order_by("-resenas_creadoras", "-rating_promedio")[:4]
        )
        panels.append({"categoria": categoria, "productos": productos})
    return render(request, "tienda/home.html", {"panels": panels})

from django.shortcuts import render, get_object_or_404
from django.db.models import Avg, Count, Case, When, IntegerField

from tienda.models import Categoria, Producto


def _productos_con_ranking(queryset):
    return (
        queryset.annotate(
            rating_promedio=Avg("resenas__calificacion"),
            total_resenas=Count("resenas"),
            resenas_creadoras=Count(
                Case(When(resenas__es_creadora=True, then=1), output_field=IntegerField())
            ),
        ).order_by("-resenas_creadoras", "-rating_promedio", "-total_resenas")
    )


def _mejor_resena(producto):
    return (
        producto.resenas.exclude(comentario="")
        .order_by("-es_creadora", "-calificacion")
        .first()
    )


def home(request):
    categorias = Categoria.objects.all()

    top_productos = list(_productos_con_ranking(Producto.objects.all())[:10])
    for producto in top_productos:
        producto.mejor_resena = _mejor_resena(producto)

    return render(request, "tienda/home.html", {
        "categorias": categorias,
        "top_productos": top_productos,
    })


def categoria_detalle(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    productos = list(_productos_con_ranking(Producto.objects.filter(categoria=categoria)))
    for producto in productos:
        producto.mejor_resena = _mejor_resena(producto)

    return render(request, "tienda/categoria.html", {
        "categoria": categoria,
        "productos": productos,
    })