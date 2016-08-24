/**
 * Created by pmmr on 23/08/2016.
 */

function setAll(){
    $('#id_total_orden_compra').autoNumeric('set', get_total_orden_compra());
}

django.jQuery(document).ready(function(){

    $('.auto').autoNumeric('init', {aSign: '  GS', pSign: 's', mDec:0});
    setAll();

    $("#ordencompra_form").submit(function(event){
        $('.auto').each(function(){
            $(this).val($(this).autoNumeric('get'));
        });
    });
});

function get_total_orden_compra(){
    var total = 0;
    $('input[name$=-total_producto_orden_compra]').each(function(){
        if (this.value())
            total+=parseInt($(this).autoNumeric('get'));
    });
    return total;
}

function get_total_producto(){
    var total = 0;

}