/**
 * Created by pmmr on 13/08/2016.
 */
(function($) {
    $(document).ready(function() {
        $(".field-precio_producto_pedido input, .field-cantidad_producto_pedido input").blur(function (event) {
            var valor = $(event.target);
            var columna = valor.parent();
            var fila = columna.parent();

            var total_producto = $('.field-total_producto_pedido input', fila);
            var precio_producto = $('.field-precio_producto_pedido input', fila);
            var cantidad_producto = $('.field-cantidad_producto_pedido input', fila);
            var total_pedido = $('#id_total_pedido');
            total_producto.val(precio_producto.val() * cantidad_producto.val());
            var suma = 0;
            var totales = $(".field-total_producto_pedido input");

            for (var i = 0; i < totales.length; i++) {
                suma += parseFloat($(totales[i]).val());
            }
            total_pedido.val(suma);
        });

        /*
        * Cuando se hace clic en el link de Eliminar al cargar una nueva Orden de Compra o se activa el check de Eliminar cuando se modifica una Orden de Compra
        * se debe restar el valor de "field-total_producto_orden_compra" de ese item al valor de "id_total_orden_compra"
        */
                //JavaScript
        $('input[type=checkbox]').on('change', function() {
            var suma = 0;
            $('input[type=checkbox]').each(function (key, value) {
                var a = $(value).is(':checked');
                if (a == false) {
                    suma = suma + parseFloat(value.parentElement.parentElement.children[3].children[0].value)
                }
            });
            $('#id_total_pedido').val(suma);
        });

        $(".field-total_producto_pedido input, .field-total_pedido input").attr("readonly", "readonly");
    });
})(django.jQuery);