/**
 * Created by pmmr on 25/05/2016.
 */

(function($) {
    $(document).ready(function() {
        console.log($.fn.jquery);
        $("#id_numero_orden_compra").change(function (event) {
            var boton = $('#compra_form button[name="_continue"]');
            boton.click();
        });

        $(".field-precio_producto_compra input, .field-cantidad_producto_compra input").blur(function (event) {
            var valor = $(event.target);
            var columna = valor.parent();
            var fila = columna.parent();

            var total_producto = $('.field-total_producto_compra input', fila);
            var precio_producto = $('.field-precio_producto_compra input', fila);
            var cantidad_producto = $('.field-cantidad_producto_compra input', fila);
            var total_compra = $('#id_total_compra');
            total_producto.val(precio_producto.val() * cantidad_producto.val());
            var suma = 0;
            var totales = $(".field-total_producto_compra input");

            for (var i = 0; i < totales.length; i++) {
                suma += parseFloat($(totales[i]).val());
            }
            total_compra.val(suma);
        });

        $(".field-total_producto_compra input, .field-total_compra input").attr("readonly", "readonly");
    });
})(django.jQuery);