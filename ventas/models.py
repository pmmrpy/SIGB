from django.db import models
# from django.utils import timezone

# Create your models here.


class Pedido(models.Model):
    fecha = models.DateTimeField()
    mesa = models.ForeignKey('bar.Mesa')
#    mozo =


class PedidoDetalle(models.Model):
    pedido = models.ForeignKey('Pedido')
    producto = models.ForeignKey('stock.Producto')
    cantidad_producto = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        verbose_name = 'Pedido - Detalle'
        verbose_name_plural = 'Pedidos - Detalles'