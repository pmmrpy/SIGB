-- View: inventario_por_deposito

-- DROP VIEW inventario_por_deposito;

CREATE OR REPLACE VIEW inventario_por_deposito AS 
SELECT COALESCE(DCE.id, DBP.id) as id,
COALESCE(DCE.producto, DBP.producto) as producto,
--     COALESCE(mov_entrante.deposito, mov_saliente.deposito) as deposito,
--     COALESCE(mov_entrante.cantidad_entrante, 0::numeric) as cantidad_entrante,
--     COALESCE(mov_saliente.cantidad_saliente, 0::numeric) as cantidad_saliente,
COALESCE(DCE.cantidad_existente_DCE, 0::numeric) as cant_exist_DCE,
COALESCE(DBP.cantidad_existente_DBP, 0::numeric) as cant_exist_DBP,
COALESCE(DBA.cantidad_existente_DBA, 0::numeric) as cant_exist_DBA,
COALESCE(DCO.cantidad_existente_DCO, 0::numeric) as cant_exist_DCO,
COALESCE(DBI.cantidad_existente_DBI, 0::numeric) as cant_exist_DBI,
COALESCE(DCE.cantidad_existente_DCE, 0::numeric) + COALESCE(DBP.cantidad_existente_DBP, 0::numeric) + COALESCE(DBA.cantidad_existente_DBA, 0::numeric) + COALESCE(DCO.cantidad_existente_DCO, 0::numeric) + COALESCE(DBI.cantidad_existente_DBI, 0::numeric) as cant_existente
FROM (
	SELECT COALESCE(mov_entrante_DCE.id, mov_saliente_DCE.id) as id,
	COALESCE(mov_entrante_DCE.producto, mov_saliente_DCE.producto) as producto,
	--     COALESCE(mov_entrante.deposito, mov_saliente.deposito) as deposito,
	--     COALESCE(mov_entrante.cantidad_entrante, 0::numeric) as cantidad_entrante,
	--     COALESCE(mov_saliente.cantidad_saliente, 0::numeric) as cantidad_saliente,
	COALESCE(mov_entrante_DCE.cantidad_entrante, 0::numeric) - COALESCE(mov_saliente_DCE.cantidad_saliente, 0::numeric) AS cantidad_existente_DCE
	FROM
	(
		(SELECT producto.id,
		producto.producto,
		deposito.deposito,
		sum(stock.cantidad_entrante) AS cantidad_entrante
		FROM stock_movimientostock stock
		JOIN stock_producto producto ON producto.id = stock.producto_stock_id
		JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_destino_id
-- 		WHERE stock.tipo_movimiento::text = 'CO'::text
		WHERE deposito.deposito::text = 'DCE'::text
		GROUP BY producto.id, producto.producto, deposito.deposito
		) mov_entrante_DCE
	FULL JOIN
		(SELECT producto.id,
		producto.producto,
		deposito.deposito,
		sum(stock.cantidad_saliente) AS cantidad_saliente
		FROM stock_movimientostock stock
		JOIN stock_producto producto ON producto.id = stock.producto_stock_id
		JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_origen_id
-- 		WHERE stock.tipo_movimiento::text = 'VE'::text
		WHERE deposito.deposito::text = 'DCE'::text
		GROUP BY producto.id, producto.producto, deposito.deposito
		) mov_saliente_DCE
	ON mov_entrante_DCE.id = mov_saliente_DCE.id)) DCE

	FULL JOIN

	(
	SELECT COALESCE(mov_entrante_DBP.id, mov_saliente_DBP.id) as id,
	COALESCE(mov_entrante_DBP.producto, mov_saliente_DBP.producto) as producto,
	--     COALESCE(mov_entrante.deposito, mov_saliente.deposito) as deposito,
	--     COALESCE(mov_entrante.cantidad_entrante, 0::numeric) as cantidad_entrante,
	--     COALESCE(mov_saliente.cantidad_saliente, 0::numeric) as cantidad_saliente,
	COALESCE(mov_entrante_DBP.cantidad_entrante, 0::numeric) - COALESCE(mov_saliente_DBP.cantidad_saliente, 0::numeric) AS cantidad_existente_DBP
	FROM
	(
		(SELECT producto.id,
		producto.producto,
		deposito.deposito,
		sum(stock.cantidad_entrante) AS cantidad_entrante
		FROM stock_movimientostock stock
		JOIN stock_producto producto ON producto.id = stock.producto_stock_id
		JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_destino_id
-- 		WHERE stock.tipo_movimiento::text = 'CO'::text
		WHERE deposito.deposito::text = 'DBP'::text
		GROUP BY producto.id, producto.producto, deposito.deposito
		) mov_entrante_DBP
	FULL JOIN
		(SELECT producto.id,
		producto.producto,
		deposito.deposito,
		sum(stock.cantidad_saliente) AS cantidad_saliente
		FROM stock_movimientostock stock
		JOIN stock_producto producto ON producto.id = stock.producto_stock_id
		JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_origen_id
-- 		WHERE stock.tipo_movimiento::text = 'VE'::text
		WHERE deposito.deposito::text = 'DBP'::text
		GROUP BY producto.id, producto.producto, deposito.deposito
		) mov_saliente_DBP
	ON mov_entrante_DBP.id = mov_saliente_DBP.id)) DBP

	ON DCE.id = DBP.id

	FULL JOIN

	(
	SELECT COALESCE(mov_entrante_DBA.id, mov_saliente_DBA.id) as id,
	COALESCE(mov_entrante_DBA.producto, mov_saliente_DBA.producto) as producto,
	--     COALESCE(mov_entrante.deposito, mov_saliente.deposito) as deposito,
	--     COALESCE(mov_entrante.cantidad_entrante, 0::numeric) as cantidad_entrante,
	--     COALESCE(mov_saliente.cantidad_saliente, 0::numeric) as cantidad_saliente,
	COALESCE(mov_entrante_DBA.cantidad_entrante, 0::numeric) - COALESCE(mov_saliente_DBA.cantidad_saliente, 0::numeric) AS cantidad_existente_DBA
	FROM
	(
		(SELECT producto.id,
		producto.producto,
		deposito.deposito,
		sum(stock.cantidad_entrante) AS cantidad_entrante
		FROM stock_movimientostock stock
		JOIN stock_producto producto ON producto.id = stock.producto_stock_id
		JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_destino_id
-- 		WHERE stock.tipo_movimiento::text = 'CO'::text
		WHERE deposito.deposito::text = 'DBA'::text
		GROUP BY producto.id, producto.producto, deposito.deposito
		) mov_entrante_DBA
	FULL JOIN
		(SELECT producto.id,
		producto.producto,
		deposito.deposito,
		sum(stock.cantidad_saliente) AS cantidad_saliente
		FROM stock_movimientostock stock
		JOIN stock_producto producto ON producto.id = stock.producto_stock_id
		JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_origen_id
-- 		WHERE stock.tipo_movimiento::text = 'VE'::text
		WHERE deposito.deposito::text = 'DBA'::text
		GROUP BY producto.id, producto.producto, deposito.deposito
		) mov_saliente_DBA
	ON mov_entrante_DBA.id = mov_saliente_DBA.id)) DBA

	ON DCE.id = DBA.id

	FULL JOIN

	(
	SELECT COALESCE(mov_entrante_DCO.id, mov_saliente_DCO.id) as id,
	COALESCE(mov_entrante_DCO.producto, mov_saliente_DCO.producto) as producto,
	--     COALESCE(mov_entrante.deposito, mov_saliente.deposito) as deposito,
	--     COALESCE(mov_entrante.cantidad_entrante, 0::numeric) as cantidad_entrante,
	--     COALESCE(mov_saliente.cantidad_saliente, 0::numeric) as cantidad_saliente,
	COALESCE(mov_entrante_DCO.cantidad_entrante, 0::numeric) - COALESCE(mov_saliente_DCO.cantidad_saliente, 0::numeric) AS cantidad_existente_DCO
	FROM
	(
		(SELECT producto.id,
		producto.producto,
		deposito.deposito,
		sum(stock.cantidad_entrante) AS cantidad_entrante
		FROM stock_movimientostock stock
		JOIN stock_producto producto ON producto.id = stock.producto_stock_id
		JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_destino_id
-- 		WHERE stock.tipo_movimiento::text = 'CO'::text
		WHERE deposito.deposito::text = 'DCO'::text
		GROUP BY producto.id, producto.producto, deposito.deposito
		) mov_entrante_DCO
	FULL JOIN
		(SELECT producto.id,
		producto.producto,
		deposito.deposito,
		sum(stock.cantidad_saliente) AS cantidad_saliente
		FROM stock_movimientostock stock
		JOIN stock_producto producto ON producto.id = stock.producto_stock_id
		JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_origen_id
-- 		WHERE stock.tipo_movimiento::text = 'VE'::text
		WHERE deposito.deposito::text = 'DCO'::text
		GROUP BY producto.id, producto.producto, deposito.deposito
		) mov_saliente_DCO
	ON mov_entrante_DCO.id = mov_saliente_DCO.id)) DCO

	ON DCE.id = DCO.id

	FULL JOIN

	(
	SELECT COALESCE(mov_entrante_DBI.id, mov_saliente_DBI.id) as id,
	COALESCE(mov_entrante_DBI.producto, mov_saliente_DBI.producto) as producto,
	--     COALESCE(mov_entrante.deposito, mov_saliente.deposito) as deposito,
	--     COALESCE(mov_entrante.cantidad_entrante, 0::numeric) as cantidad_entrante,
	--     COALESCE(mov_saliente.cantidad_saliente, 0::numeric) as cantidad_saliente,
	COALESCE(mov_entrante_DBI.cantidad_entrante, 0::numeric) - COALESCE(mov_saliente_DBI.cantidad_saliente, 0::numeric) AS cantidad_existente_DBI
	FROM
	(
		(SELECT producto.id,
		producto.producto,
		deposito.deposito,
		sum(stock.cantidad_entrante) AS cantidad_entrante
		FROM stock_movimientostock stock
		JOIN stock_producto producto ON producto.id = stock.producto_stock_id
		JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_destino_id
-- 		WHERE stock.tipo_movimiento::text = 'CO'::text
		WHERE deposito.deposito::text = 'DBI'::text
		GROUP BY producto.id, producto.producto, deposito.deposito
		) mov_entrante_DBI
	FULL JOIN
		(SELECT producto.id,
		producto.producto,
		deposito.deposito,
		sum(stock.cantidad_saliente) AS cantidad_saliente
		FROM stock_movimientostock stock
		JOIN stock_producto producto ON producto.id = stock.producto_stock_id
		JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_origen_id
-- 		WHERE stock.tipo_movimiento::text = 'VE'::text
		WHERE deposito.deposito::text = 'DBI'::text
		GROUP BY producto.id, producto.producto, deposito.deposito
		) mov_saliente_DBI
	ON mov_entrante_DBI.id = mov_saliente_DBI.id)) DBI

	ON DCE.id = DBI.id
	;

ALTER TABLE inventario_por_deposito
  OWNER TO postgres;
