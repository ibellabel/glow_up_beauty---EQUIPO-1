from tienda.models import Orden


class OrdenBuilderError(Exception):
    pass


class OrdenBuilder:
    def __init__(self):
        self._usuario = None
        self._productos = []

    def para_usuario(self, usuario):
        self._usuario = usuario
        return self

    def con_productos(self, productos):
        self._productos = productos
        return self

    def _validar(self):
        if self._usuario is None:
            raise OrdenBuilderError("La orden requiere un usuario.")
        if not self._productos:
            raise OrdenBuilderError("La orden requiere al menos un producto.")
        for producto in self._productos:
            if not producto.validarStock():
                raise OrdenBuilderError(
                    f"Sin stock suficiente para '{producto.nombre}'."
                )

    def build(self) -> Orden:
        self._validar()
        orden = Orden(usuario=self._usuario, estado="PENDIENTE")
        orden.save()
        orden.productos.set(self._productos)
        return orden