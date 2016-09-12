/**
 * Created by pmmr on 23/08/2016.
 */

django.jQuery(document).ready(function(){
      $('input[name$=-monto_pago_proveedor]').keyup(function (){
       var total_pago =  get_total_pago();
          var total_factura = $('#id_total_factura_compra').val();
          if (parseFloat(total_pago) > parseFloat(total_factura)){
              alert('El Monto Total de los Pagos no puede exceder al Total de la Factura.')
              this.value = parseFloat(total_factura) -(total_pago - parseFloat(this.value))
               $('#id_total_pago_factura').val(total_factura);
          }

    });

});


function get_total_pago(){
    var total = 0;
    $('input[name$=-monto_pago_proveedor]').each(function (){
        total += this.value ? parseFloat(this.value) : 0;
    });
    $('#id_total_pago_factura').val(total);
    return total
}
