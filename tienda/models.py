from django.db import models


class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    comisionPorcentaje = models.DecimalField(max_digits=5, decimal_places=2, default=10)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    tipoPiel = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name="productos")

    def validarStock(self):
        return self.stock > 0

    def calcularDescuento(self):
        return self.precio  # placeholder, ajusta si tienes lógica real

    def __str__(self):
        return self.nombre


class Orden(models.Model):
    ESTADOS = [
        ("PENDIENTE", "Pendiente"),
        ("CONFIRMADA", "Confirmada"),
    ]
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="ordenes")
    productos = models.ManyToManyField(Producto, related_name="ordenes")
    estado = models.CharField(max_length=20, choices=ESTADOS, default="PENDIENTE")
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calcularTotal(self):
        self.total = sum(p.precio for p in self.productos.all())
        self.save()
        return self.total

    def repartirComisionMarca(self):
        # placeholder simple: imprime la comisión por marca involucrada
        for producto in self.productos.all():
            comision = producto.precio * (producto.marca.comisionPorcentaje / 100)
            print(f"Comisión para {producto.marca.nombre}: {comision}")

    def procesarPago(self):
        # placeholder: aquí iría integración de pago real
        print(f"Pago procesado para orden #{self.id} — total: {self.total}")

    def __str__(self):
        return f"Orden #{self.id} - {self.estado}"