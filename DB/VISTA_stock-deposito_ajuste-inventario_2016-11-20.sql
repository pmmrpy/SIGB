-- DROP VIEW stock_por_deposito_para_ajuste_inventario;

-- CREATE OR REPLACE VIEW stock_por_deposito_para_ajuste_inventario AS  (

SELECT COALESCE(mov_entrante_dce.producto_id, mov_saliente_dce.producto_id) AS id,
COALESCE(mov_entrante_dce.producto, mov_saliente_dce.producto) AS producto,
COALESCE(mov_entrante_dce.deposito_id, mov_saliente_dce.deposito_id) AS deposito_id,            
COALESCE(mov_entrante_dce.cantidad_entrante, 0::numeric) - COALESCE(mov_saliente_dce.cantidad_saliente, 0::numeric) AS cantidad_existente
FROM
(SELECT producto.id as producto_id,
	producto.producto,
	deposito.id as deposito_id,
	sum(stock.cantidad_entrante) AS cantidad_entrante
	FROM stock_movimientostock stock
	JOIN stock_producto producto ON producto.id = stock.producto_stock_id
	JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_destino_id
	WHERE deposito.deposito::text = 'DCE'::text
	GROUP BY producto.id, producto.producto, deposito.id) mov_entrante_dce
FULL JOIN
(SELECT producto.id as producto_id,
	producto.producto,
	deposito.id as deposito_id,
	sum(stock.cantidad_saliente) AS cantidad_saliente
	FROM stock_movimientostock stock
	JOIN stock_producto producto ON producto.id = stock.producto_stock_id
	JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_origen_id
	WHERE deposito.deposito::text = 'DCE'::text
	GROUP BY producto.id, producto.producto, deposito.id) mov_saliente_dce
ON mov_entrante_dce.producto_id = mov_saliente_dce.producto_id

UNION

SELECT COALESCE(mov_entrante_dbp.producto_id, mov_saliente_dbp.producto_id) AS producto_id,
COALESCE(mov_entrante_dbp.producto, mov_saliente_dbp.producto) AS producto,
COALESCE(mov_entrante_dbp.deposito_id, mov_saliente_dbp.deposito_id) AS deposito_id,            
COALESCE(mov_entrante_dbp.cantidad_entrante, 0::numeric) - COALESCE(mov_saliente_dbp.cantidad_saliente, 0::numeric) AS cantidad_existente
FROM
(SELECT producto.id as producto_id,
	producto.producto,
	deposito.id as deposito_id,
	sum(stock.cantidad_entrante) AS cantidad_entrante
	FROM stock_movimientostock stock
	JOIN stock_producto producto ON producto.id = stock.producto_stock_id
	JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_destino_id
	WHERE deposito.deposito::text = 'DBP'::text
	GROUP BY producto.id, producto.producto, deposito.id) mov_entrante_dbp
FULL JOIN
(SELECT producto.id as producto_id,
	producto.producto,
	deposito.id as deposito_id,
	sum(stock.cantidad_saliente) AS cantidad_saliente
	FROM stock_movimientostock stock
	JOIN stock_producto producto ON producto.id = stock.producto_stock_id
	JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_origen_id
	WHERE deposito.deposito::text = 'DBP'::text
	GROUP BY producto.id, producto.producto, deposito.id) mov_saliente_dbp
ON mov_entrante_dbp.producto_id = mov_saliente_dbp.producto_id
-- ON dce.producto_id = dbp.producto_id and dce.producto = dbp.producto and dce.deposito_id = dbp.deposito_id and dce.cantidad_existente = dbp.cantidad_existente

UNION

SELECT COALESCE(mov_entrante_dba.producto_id, mov_saliente_dba.producto_id) AS producto_id,
COALESCE(mov_entrante_dba.producto, mov_saliente_dba.producto) AS producto,
COALESCE(mov_entrante_dba.deposito_id, mov_saliente_dba.deposito_id) AS deposito_id,            
COALESCE(mov_entrante_dba.cantidad_entrante, 0::numeric) - COALESCE(mov_saliente_dba.cantidad_saliente, 0::numeric) AS cantidad_existente
FROM
(SELECT producto.id as producto_id,
	producto.producto,
	deposito.id as deposito_id,
	sum(stock.cantidad_entrante) AS cantidad_entrante
	FROM stock_movimientostock stock
	JOIN stock_producto producto ON producto.id = stock.producto_stock_id
	JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_destino_id
	WHERE deposito.deposito::text = 'DBA'::text
	GROUP BY producto.id, producto.producto, deposito.id) mov_entrante_dba
FULL JOIN
(SELECT producto.id as producto_id,
	producto.producto,
	deposito.id as deposito_id,
	sum(stock.cantidad_saliente) AS cantidad_saliente
	FROM stock_movimientostock stock
	JOIN stock_producto producto ON producto.id = stock.producto_stock_id
	JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_origen_id
	WHERE deposito.deposito::text = 'DBA'::text
	GROUP BY producto.id, producto.producto, deposito.id) mov_saliente_dba
ON mov_entrante_dba.producto_id = mov_saliente_dba.producto_id

UNION

SELECT COALESCE(mov_entrante_dco.producto_id, mov_saliente_dco.producto_id) AS producto_id,
COALESCE(mov_entrante_dco.producto, mov_saliente_dco.producto) AS producto,
COALESCE(mov_entrante_dco.deposito_id, mov_saliente_dco.deposito_id) AS deposito_id,            
COALESCE(mov_entrante_dco.cantidad_entrante, 0::numeric) - COALESCE(mov_saliente_dco.cantidad_saliente, 0::numeric) AS cantidad_existente
FROM
(SELECT producto.id as producto_id,
	producto.producto,
	deposito.id as deposito_id,
	sum(stock.cantidad_entrante) AS cantidad_entrante
	FROM stock_movimientostock stock
	JOIN stock_producto producto ON producto.id = stock.producto_stock_id
	JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_destino_id
	WHERE deposito.deposito::text = 'DCO'::text
	GROUP BY producto.id, producto.producto, deposito.id) mov_entrante_dco
FULL JOIN
(SELECT producto.id as producto_id,
	producto.producto,
	deposito.id as deposito_id,
	sum(stock.cantidad_saliente) AS cantidad_saliente
	FROM stock_movimientostock stock
	JOIN stock_producto producto ON producto.id = stock.producto_stock_id
	JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_origen_id
	WHERE deposito.deposito::text = 'DCO'::text
	GROUP BY producto.id, producto.producto, deposito.id) mov_saliente_dco
ON mov_entrante_dco.producto_id = mov_saliente_dco.producto_id

UNION

SELECT COALESCE(mov_entrante_dbi.producto_id, mov_saliente_dbi.producto_id) AS producto_id,
COALESCE(mov_entrante_dbi.producto, mov_saliente_dbi.producto) AS producto,
COALESCE(mov_entrante_dbi.deposito_id, mov_saliente_dbi.deposito_id) AS deposito_id,            
COALESCE(mov_entrante_dbi.cantidad_entrante, 0::numeric) - COALESCE(mov_saliente_dbi.cantidad_saliente, 0::numeric) AS cantidad_existente
FROM
(SELECT producto.id as producto_id,
	producto.producto,
	deposito.id as deposito_id,
	sum(stock.cantidad_entrante) AS cantidad_entrante
	FROM stock_movimientostock stock
	JOIN stock_producto producto ON producto.id = stock.producto_stock_id
	JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_destino_id
	WHERE deposito.deposito::text = 'DBI'::text
	GROUP BY producto.id, producto.producto, deposito.id) mov_entrante_dbi
FULL JOIN
(SELECT producto.id as producto_id,
	producto.producto,
	deposito.id as deposito_id,
	sum(stock.cantidad_saliente) AS cantidad_saliente
	FROM stock_movimientostock stock
	JOIN stock_producto producto ON producto.id = stock.producto_stock_id
	JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_origen_id
	WHERE deposito.deposito::text = 'DBI'::text
	GROUP BY producto.id, producto.producto, deposito.id) mov_saliente_dbi
ON mov_entrante_dbi.producto_id = mov_saliente_dbi.producto_id

ORDER BY producto, deposito_id
-- )