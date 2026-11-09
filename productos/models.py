from django.db import models

class categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class productos(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=60)
    categoria = models.ForeignKey(
        categoria,
        on_delete=models.CASCADE,
        related_name='productos'
    )
    talla = models.CharField(max_length=15)
    color = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f'{self.nombre} - {self.marca}'


class clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class venta(models.Model):
    cliente = models.ForeignKey(
        clientes,
        on_delete=models.CASCADE,
        related_name='ventas'
    )
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Venta {self.id} - {self.cliente}'


class Detalleventa(models.Model):
    venta = models.ForeignKey(
        venta,
        on_delete=models.CASCADE,
        related_name='detalles'
    )
    producto = models.ForeignKey(
        productos,
        on_delete=models.CASCADE
    )
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)

    @property
    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f'{self.venta} - {self.producto} - {self.cantidad}'
