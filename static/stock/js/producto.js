/**
 * Created by pmmr on 22/06/2016.
 */

django.jQuery(document).ready(function(){
    if (document.getElementById("id_tipo_producto").value == 'IN'){
        $('#id_porcentaje_ganancia').prop('readonly', true);
        $('#id_precio_venta_sugerido').prop('readonly', true);
        $('#id_precio_venta').prop('readonly', true);
    }else{
        $('#id_porcentaje_ganancia').removeAttr('readonly');
        set_precio_venta_sugerido();
        $('#id_precio_venta_sugerido').prop('readonly', true);
        $('#id_precio_venta').removeAttr('readonly');
    }

    $("#id_tipo_producto").change(function(){
      if (this.value == 'IN'){
          $('#id_porcentaje_ganancia').prop('readonly', true).val(0);
          $('#id_precio_venta_sugerido').prop('readonly', true).val(0);
          $('#id_precio_venta').prop('readonly', true).val(0);
      }else{
          $('#id_porcentaje_ganancia').removeAttr('readonly');
          set_precio_venta_sugerido();
          $('#id_precio_venta_sugerido').prop('readonly', true);
          $('#id_precio_venta').removeAttr('readonly');
      }
    });

    $('input[name=porcentaje_ganancia]').keyup(function (){
        //var indice = this.name.split('-')[1];
        //var cantidad = $('#id_ordencompradetalle_set-'+indice+'-cantidad_producto_orden_compra').val();
        //var total =  ((this.value)? parseFloat(this.value) : 0)*(cantidad? cantidad : 0);
        //$('#id_ordencompradetalle_set-'+indice+'-total_producto_orden_compra').val(total)
        //set_total();
        //alert('Entro a id_porcentaje_ganancia.keyup');
        //var porcentaje =  ((this.value)? parseFloat(this.value) : 0);
        //var porcentaje =  this.val();
        set_precio_venta_sugerido();
    });

    $('input[name=precio_compra]').keyup(function (){
        var precio_compra_sugerido = (($('#id_precio_compra_sugerido').val())? ($('#id_precio_compra_sugerido').val()) : 0);
        if (parseFloat(precio_compra_sugerido) == 0){
            set_precio_venta_sugerido();
        }
    });

    $('#id_categoria').change(function(){
        $('#id_subcategoria').val('');
        $('#select2-id_subcategoria-container').html('');
    });

});

function set_precio_venta_sugerido(){
    var precio_compra_sugerido = (($('#id_precio_compra_sugerido').val())? ($('#id_precio_compra_sugerido').val()) : 0);
    if (parseFloat(precio_compra_sugerido) == 0){
        precio_compra_sugerido = (($('#id_precio_compra').val())? ($('#id_precio_compra').val()) : 0)
    }
    //var porcentaje_ganancia = ($('#id_porcentaje_ganancia').value()? parseFloat($('#id_porcentaje_ganancia').value) : 0);
    var porcentaje_ganancia = $('#id_porcentaje_ganancia').val();
    //var porcentaje_ganancia = porcentaje;
    var precio_venta_sugerido = parseFloat((precio_compra_sugerido * porcentaje_ganancia) / 100) + parseFloat(precio_compra_sugerido);
    //alert(precio_compra_sugerido);
    //alert(porcentaje_ganancia);
    //alert(precio_venta_sugerido);
    $('#id_precio_venta_sugerido').val(precio_venta_sugerido);
}