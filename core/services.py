from core.domain.orden_builder import OrdenBuilder
from core.infra.notificador_factory import NotificadorFactory
from tienda.models import Producto


class OrdenService:
    def __init__(self, notificador=None):
        self.notificador = notificador or NotificadorFactory.crear()

    def crear_orden(self, usuario, productos_ids):
        # Obtiene los productos seleccionados
        productos = Producto.objects.filter(id__in=productos_ids)

        # Construye la orden
        orden = (
            OrdenBuilder()
            .para_usuario(usuario)
            .con_productos(productos)
            .build()
        )

        # Procesa la orden
        orden.calcularTotal()
        orden.repartirComisionMarca()
        orden.procesarPago()

        # Cambia el estado a confirmada
        orden.estado = "CONFIRMADA"
        orden.save()

        # Envía la notificación
        self.notificador.enviar_confirmacion(orden)

        return orden