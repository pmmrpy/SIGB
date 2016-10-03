CREATE VIEW inventario_por_producto AS (
select COMPRAS.id, COMPRAS.producto,(coalesce(COMPRAS.stock,0 ) - coalesce(VENTAS.stock,0)) as stock from (
select producto.id,producto.producto,sum(detalle.cantidad_entrante) stock from stock_stock stock
join stock_stockdetalle detalle on stock.id = detalle.stock_id
join stock_producto producto on producto.id = producto_stock_id
join bar_tipomovimientostock movimiento on movimiento.id = detalle.tipo_movimiento_id
where movimiento.tipo_movimiento_stock = 'CO'

group by producto.id,producto.producto,detalle.cantidad_entrante

) as COMPRAS full outer join (
select producto.id,producto.producto,sum(detalle.cantidad_saliente) as stock from stock_stock stock
join stock_stockdetalle detalle on stock.id = detalle.stock_id
join stock_producto producto on producto.id = producto_stock_id
join bar_tipomovimientostock movimiento on movimiento.id = detalle.tipo_movimiento_id
where movimiento.tipo_movimiento_stock = 'VE'
group by producto.id,producto.producto,detalle.cantidad_saliente

) as VENTAS on VENTAS.id = COMPRAS.id
)