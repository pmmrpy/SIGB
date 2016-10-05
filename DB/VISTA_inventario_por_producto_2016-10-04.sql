--CREATE VIEW inventario_por_producto AS (

select COMPRAS.id, COMPRAS.producto, COMPRAS.total_compras, VENTAS.total_ventas, (coalesce(COMPRAS.total_compras, 0) - coalesce(VENTAS.total_ventas, 0)) as cantidad_existente
from 

(
select producto.id, producto.producto, sum(stock.cantidad_entrante) as total_compras from stock_movimientostock stock
join stock_producto producto on producto.id = stock.producto_stock_id
where stock.tipo_movimiento = 'CO'

group by producto.id, producto.producto
) as COMPRAS

full outer join

(
select producto.id, producto.producto, sum(stock.cantidad_saliente) as total_ventas from stock_movimientostock stock
join stock_producto producto on producto.id = stock.producto_stock_id
where stock.tipo_movimiento = 'VE'

group by producto.id, producto.producto
) as VENTAS

on VENTAS.id = COMPRAS.id

--)