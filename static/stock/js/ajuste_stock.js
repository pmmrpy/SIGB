/**
 * Created by pmmr on 20/11/2016.
 */

django.jQuery(document).ready(function(){

    $("#id_deposito").change(function(){
        //alert('Cambio id_proveedor_orden_pago');
        var boton = $('#ajustestock_form button[name="_continue"]');
        boton.click();
    });

    $('input[type=checkbox]').on('change', function() {
        var indice = this.name.split('-')[1];
        if ($('#id_ajustestockdetalle_set-'+indice+'-ajustar').is(':checked') == true){
            $('#id_ajustestockdetalle_set-'+indice+'-cantidad_ajustar_producto').removeAttr('readonly').val('');
            $('#id_ajustestockdetalle_set-'+indice+'-motivo_ajuste').removeAttr('readonly').val('');

        } else if ($('#id_ajustestockdetalle_set-'+indice+'-ajustar').is(':checked') == false){
            $('#id_ajustestockdetalle_set-'+indice+'-cantidad_ajustar_producto').prop('readonly', true).val('');
            $('#id_ajustestockdetalle_set-'+indice+'-motivo_ajuste').prop('readonly', true).val('');
        }
    });

});
