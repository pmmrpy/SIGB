-- View: inventario_por_deposito

-- DROP VIEW inventario_por_deposito;

CREATE OR REPLACE VIEW inventario_por_deposito AS 
 SELECT COALESCE(dce.id, dbp.id, dba.id, dco.id, dbi.id) AS id,
    COALESCE(dce.producto, dbp.producto, dba.producto, dco.producto, dbi.producto) AS producto,
    COALESCE(dce.cantidad_existente_dce, 0::numeric) AS cant_exist_dce,
    COALESCE(dbp.cantidad_existente_dbp, 0::numeric) AS cant_exist_dbp,
    COALESCE(dba.cantidad_existente_dba, 0::numeric) AS cant_exist_dba,
    COALESCE(dco.cantidad_existente_dco, 0::numeric) AS cant_exist_dco,
    COALESCE(dbi.cantidad_existente_dbi, 0::numeric) AS cant_exist_dbi,
    COALESCE(dce.cantidad_existente_dce, 0::numeric) + COALESCE(dbp.cantidad_existente_dbp, 0::numeric) + COALESCE(dba.cantidad_existente_dba, 0::numeric) + COALESCE(dco.cantidad_existente_dco, 0::numeric) + COALESCE(dbi.cantidad_existente_dbi, 0::numeric) AS cant_existente
   FROM ( SELECT COALESCE(mov_entrante_dce.id, mov_saliente_dce.id) AS id,
            COALESCE(mov_entrante_dce.producto, mov_saliente_dce.producto) AS producto,
            COALESCE(mov_entrante_dce.cantidad_entrante, 0::numeric) - COALESCE(mov_saliente_dce.cantidad_saliente, 0::numeric) AS cantidad_existente_dce
           FROM ( SELECT producto.id,
                    producto.producto,
                    deposito.deposito,
                    sum(stock.cantidad_entrante) AS cantidad_entrante
                   FROM stock_movimientostock stock
                     JOIN stock_producto producto ON producto.id = stock.producto_stock_id
                     JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_destino_id
                  WHERE deposito.deposito::text = 'DCE'::text
                  GROUP BY producto.id, producto.producto, deposito.deposito) mov_entrante_dce
             FULL JOIN ( SELECT producto.id,
                    producto.producto,
                    deposito.deposito,
                    sum(stock.cantidad_saliente) AS cantidad_saliente
                   FROM stock_movimientostock stock
                     JOIN stock_producto producto ON producto.id = stock.producto_stock_id
                     JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_origen_id
                  WHERE deposito.deposito::text = 'DCE'::text
                  GROUP BY producto.id, producto.producto, deposito.deposito) mov_saliente_dce ON mov_entrante_dce.id = mov_saliente_dce.id) dce
     FULL JOIN ( SELECT COALESCE(mov_entrante_dbp.id, mov_saliente_dbp.id) AS id,
            COALESCE(mov_entrante_dbp.producto, mov_saliente_dbp.producto) AS producto,
            COALESCE(mov_entrante_dbp.cantidad_entrante, 0::numeric) - COALESCE(mov_saliente_dbp.cantidad_saliente, 0::numeric) AS cantidad_existente_dbp
           FROM ( SELECT producto.id,
                    producto.producto,
                    deposito.deposito,
                    sum(stock.cantidad_entrante) AS cantidad_entrante
                   FROM stock_movimientostock stock
                     JOIN stock_producto producto ON producto.id = stock.producto_stock_id
                     JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_destino_id
                  WHERE deposito.deposito::text = 'DBP'::text
                  GROUP BY producto.id, producto.producto, deposito.deposito) mov_entrante_dbp
             FULL JOIN ( SELECT producto.id,
                    producto.producto,
                    deposito.deposito,
                    sum(stock.cantidad_saliente) AS cantidad_saliente
                   FROM stock_movimientostock stock
                     JOIN stock_producto producto ON producto.id = stock.producto_stock_id
                     JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_origen_id
                  WHERE deposito.deposito::text = 'DBP'::text
                  GROUP BY producto.id, producto.producto, deposito.deposito) mov_saliente_dbp ON mov_entrante_dbp.id = mov_saliente_dbp.id) dbp ON dce.id = dbp.id
     FULL JOIN ( SELECT COALESCE(mov_entrante_dba.id, mov_saliente_dba.id) AS id,
            COALESCE(mov_entrante_dba.producto, mov_saliente_dba.producto) AS producto,
            COALESCE(mov_entrante_dba.cantidad_entrante, 0::numeric) - COALESCE(mov_saliente_dba.cantidad_saliente, 0::numeric) AS cantidad_existente_dba
           FROM ( SELECT producto.id,
                    producto.producto,
                    deposito.deposito,
                    sum(stock.cantidad_entrante) AS cantidad_entrante
                   FROM stock_movimientostock stock
                     JOIN stock_producto producto ON producto.id = stock.producto_stock_id
                     JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_destino_id
                  WHERE deposito.deposito::text = 'DBA'::text
                  GROUP BY producto.id, producto.producto, deposito.deposito) mov_entrante_dba
             FULL JOIN ( SELECT producto.id,
                    producto.producto,
                    deposito.deposito,
                    sum(stock.cantidad_saliente) AS cantidad_saliente
                   FROM stock_movimientostock stock
                     JOIN stock_producto producto ON producto.id = stock.producto_stock_id
                     JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_origen_id
                  WHERE deposito.deposito::text = 'DBA'::text
                  GROUP BY producto.id, producto.producto, deposito.deposito) mov_saliente_dba ON mov_entrante_dba.id = mov_saliente_dba.id) dba ON dce.id = dba.id
     FULL JOIN ( SELECT COALESCE(mov_entrante_dco.id, mov_saliente_dco.id) AS id,
            COALESCE(mov_entrante_dco.producto, mov_saliente_dco.producto) AS producto,
            COALESCE(mov_entrante_dco.cantidad_entrante, 0::numeric) - COALESCE(mov_saliente_dco.cantidad_saliente, 0::numeric) AS cantidad_existente_dco
           FROM ( SELECT producto.id,
                    producto.producto,
                    deposito.deposito,
                    sum(stock.cantidad_entrante) AS cantidad_entrante
                   FROM stock_movimientostock stock
                     JOIN stock_producto producto ON producto.id = stock.producto_stock_id
                     JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_destino_id
                  WHERE deposito.deposito::text = 'DCO'::text
                  GROUP BY producto.id, producto.producto, deposito.deposito) mov_entrante_dco
             FULL JOIN ( SELECT producto.id,
                    producto.producto,
                    deposito.deposito,
                    sum(stock.cantidad_saliente) AS cantidad_saliente
                   FROM stock_movimientostock stock
                     JOIN stock_producto producto ON producto.id = stock.producto_stock_id
                     JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_origen_id
                  WHERE deposito.deposito::text = 'DCO'::text
                  GROUP BY producto.id, producto.producto, deposito.deposito) mov_saliente_dco ON mov_entrante_dco.id = mov_saliente_dco.id) dco ON dce.id = dco.id
     FULL JOIN ( SELECT COALESCE(mov_entrante_dbi.id, mov_saliente_dbi.id) AS id,
            COALESCE(mov_entrante_dbi.producto, mov_saliente_dbi.producto) AS producto,
            COALESCE(mov_entrante_dbi.cantidad_entrante, 0::numeric) - COALESCE(mov_saliente_dbi.cantidad_saliente, 0::numeric) AS cantidad_existente_dbi
           FROM ( SELECT producto.id,
                    producto.producto,
                    deposito.deposito,
                    sum(stock.cantidad_entrante) AS cantidad_entrante
                   FROM stock_movimientostock stock
                     JOIN stock_producto producto ON producto.id = stock.producto_stock_id
                     JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_destino_id
                  WHERE deposito.deposito::text = 'DBI'::text
                  GROUP BY producto.id, producto.producto, deposito.deposito) mov_entrante_dbi
             FULL JOIN ( SELECT producto.id,
                    producto.producto,
                    deposito.deposito,
                    sum(stock.cantidad_saliente) AS cantidad_saliente
                   FROM stock_movimientostock stock
                     JOIN stock_producto producto ON producto.id = stock.producto_stock_id
                     JOIN bar_deposito deposito ON deposito.id = stock.ubicacion_origen_id
                  WHERE deposito.deposito::text = 'DBI'::text
                  GROUP BY producto.id, producto.producto, deposito.deposito) mov_saliente_dbi ON mov_entrante_dbi.id = mov_saliente_dbi.id) dbi ON dce.id = dbi.id;

ALTER TABLE inventario_por_deposito
  OWNER TO postgres;
