/**
 * Created by pmmr on 23/08/2016.
 */

django.jQuery(document).ready(function(){

    $('input[name$=-precio_producto_orden_compra]').keyup(function (){
        var indice = this.name.split('-')[1];
        var cantidad = $('#id_ordencompradetalle_set-'+indice+'-cantidad_producto_orden_compra').val();
        var total =  ((this.value)? parseFloat(this.value) : 0)*(cantidad? cantidad : 0);
        $('#id_ordencompradetalle_set-'+indice+'-total_producto_orden_compra').val(total)
        set_total();
    });

    $('input[name$=-cantidad_producto_orden_compra]').keyup(function (){
        var indice = this.name.split('-')[1];
        var precio = $('#id_ordencompradetalle_set-'+indice+'-precio_producto_orden_compra').val();
        var total =  ((this.value)? parseFloat(this.value) : 0)*(precio? precio : 0);
        $('#id_ordencompradetalle_set-'+indice+'-total_producto_orden_compra').val(total)
        set_total();
    });

     $('input[type=checkbox]').on('change', function() {
         alert('asdfasdf')
            //var suma = 0;
            //$('input[type=checkbox]').each(function (key, value) {
            //    var a = $(value).is(':checked');
            //    if (a == false) {
            //        suma = suma + parseFloat(value.parentElement.parentElement.children[3].children[0].value)
            //    }
            //});
            //$('#id_total_orden_compra').val(suma);
        });



     $('input[id$=-producto_orden_compra]').on('change',function(){
         alert('asdf')
     })

});

function set_total(){
    var total = 0;
    $('input[name$=-total_producto_orden_compra]').each(function (){
        total += this.value ? parseFloat(this.value) : 0;
    });
    $('#id_total_orden_compra').val(total);
}
