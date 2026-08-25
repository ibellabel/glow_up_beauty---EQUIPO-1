from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from tienda.models import Producto, Categoria, Resena, DireccionEnvio
from core.serializers import (
    ProductoSerializer,
    CategoriaSerializer,
    ResenaSerializer,
    DireccionEnvioSerializer,
)


class ProductoListView(APIView):
    """Endpoint de solo lectura para listar productos (catálogo).
    Sin lógica de negocio: solo consulta y serializa.
    """

    def get(self, request):
        productos = Producto.objects.select_related("marca", "categoria").all()
        return Response(ProductoSerializer(productos, many=True).data, status=status.HTTP_200_OK)


class CategoriaListView(APIView):
    """Listado simple de categorías. Sin lógica de negocio."""

    def get(self, request):
        categorias = Categoria.objects.all()
        return Response(CategoriaSerializer(categorias, many=True).data, status=status.HTTP_200_OK)


class ResenaListCreateView(APIView):
    

    def get(self, request):
        resenas = Resena.objects.select_related("usuario", "producto").all()
        return Response(ResenaSerializer(resenas, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ResenaSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DireccionEnvioListCreateView(APIView):
    """Listar y crear direcciones de envío de un usuario."""

    def get(self, request):
        direcciones = DireccionEnvio.objects.select_related("usuario").all()
        return Response(DireccionEnvioSerializer(direcciones, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DireccionEnvioSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)