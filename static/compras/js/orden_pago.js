/**
 * Created by pmmr on 19/09/2016.
 */

django.jQuery(document).ready(function(){

    console.log($.fn.jquery);

    $("#id_proveedor_orden_pago").change(function(){
        //alert('Cambio id_proveedor_orden_pago');
        var boton = $('#ordenpago_form button[name="_continue"]');
        boton.click();
    });

    $('input[type=checkbox]').on('change', function() {
        var suma = 0;
        $('input[type=checkbox]').each(function (key, value) {
            var indice = this.name.split('-')[1];
            var monto_factura = $('#id_ordenpagodetalle_set-'+indice+'-total_factura_compra').val();
            var a = $(value).is(':checked');
            if (a == true) {
                suma = suma + parseFloat(monto_factura)
            }
        });
        $('#id_total_orden_pago').val(suma);
    });

    $(".field-total_factura_compra input").attr("readonly", true);

});