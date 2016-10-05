/**
 * Created by pmmr on 13/08/2016.
 */
django.jQuery(document).ready(function(){
//(function($) {
//    $(document).ready(function() {

    $('input[name$=-cantidad_producto_pedido]').keyup(function (){
        var indice = this.name.split('-')[1];
        var precio = $('#id_pedidodetalle_set-'+indice+'-precio_producto_pedido').val();
        var total =  ((this.value)? parseFloat(this.value) : 0)*(precio? precio : 0);
        $('#id_pedidodetalle_set-'+indice+'-total_producto_pedido').val(total);
        set_total();
    });

     $('#id_reserva').change(function (){
         set_reserva(this.value);
     });

    /*
    * Cuando se hace clic en el link de Eliminar al cargar una nueva Orden de Compra o se activa el check de Eliminar cuando se modifica una Orden de Compra
    * se debe restar el valor de "field-total_producto_orden_compra" de ese item al valor de "id_total_orden_compra"
    */
            //JavaScript
    //$('input[type=checkbox]').on('change', function() {
    //    var suma = 0;
    //    $('input[type=checkbox]').each(function (key, value) {
    //        var a = $(value).is(':checked');
    //        if (a == false) {
    //            suma = suma + parseFloat(value.parentElement.parentElement.children[3].children[0].value)
    //        }
    //    });
    //    $('#id_total_pedido').val(suma);
    //});

    $('input[type=checkbox]').on('change', function() {
        var suma = 0;
        $('input[type=checkbox]').each(function (key, value) {
            var indice = this.name.split('-')[1];
            var total_producto = $('#id_pedidodetalle_set-'+indice+'-total_producto_pedido').val();
            var a = $(value).is(':checked');
            if (a == false) {
                suma = suma + parseFloat(total_producto)
            }
        });
        $('#id_total_pedido').val(suma);
    });

    $(".field-precio_producto_pedido input, .field-total_producto_pedido input, .field-total_pedido input").attr("readonly", "readonly");
    //$('#id_reserva').attr("readonly", "readonly");
    //});
//})(django.jQuery);
});

// Retorna los valores del raw_id_fields
function dismissRelatedLookupPopup(win, chosenId) {
    var name = windowname_to_id(win.name);
    var elem = document.getElementById(name);
    if (elem.className.indexOf('vManyToManyRawIdAdminField') != -1 && elem.value) {
        elem.value += ',' + chosenId;
    } else {
        document.getElementById(name).value = chosenId;
    }
    win.close();
    //alert('name: ' + name + ' - chosenId: ' + chosenId)
    //if (chosenId)
    //   set_producto_detalle(chosenId,name);
    if (name == 'id_reserva'){
        set_reserva(chosenId);
    } else {
        set_producto_detalle(chosenId,name);
    }
}

function set_producto_detalle(id_producto,name) {
    $.ajax({
        url : "/stock/get_producto_venta_detalle/", // the endpoint
        type : "GET", // http method
        data : { id_producto : id_producto }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            var indice = name.split('-')[1];
            //alert(JSON.stringify(json));

            $('#id_pedidodetalle_set-'+indice+'-precio_producto_pedido').val(json.precio_venta);
            //$(".field-unidad_medida_orden_compra select").attr("disabled", false);
            //$('#id_ordencompradetalle_set-'+indice+'-unidad_medida_orden_compra').val(json.unidad_medida_producto_id);
            //$('#id_ordencompradetalle_set-'+indice+'-unidad_medida_orden_compra').val(json.unidad_medida_producto_display);
            $('#id_pedidodetalle_set-'+indice+'-cantidad_producto_pedido').val('1');
            $('#id_pedidodetalle_set-'+indice+'-total_producto_pedido').val(json.precio_venta);
            set_total();

            //alert($('#lookup_id_ordencompradetalle_set-'+indice+'-producto_orden_compra').());
//)
            $('#lookup_id_pedidodetalle_set-'+indice+'-producto_pedido').after('<strong>'+json.producto+'</strong>');
            //var parent = $('#lookup_id_ordencompradetalle_set-'+indice+'-producto_orden_compra');
            //alert(JSON.stringify(parent.html()))
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });

    //$(".field-unidad_medida_orden_compra select").attr("disabled", true);
}

function set_reserva(id_reserva) {
        $.ajax({
        url : "/ventas/get_reserva/", // the endpoint
        type : "GET", // http method
        data : { id_reserva : id_reserva }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            //var indice = name.split('-')[1];
            alert(JSON.stringify(json));

            $('#id_id_cliente_reserva').val(json.cliente.id);
            $('#id_cliente_reserva').val(json.cliente.nombre_cliente);
            $('#id_doc_ruc_cliente_reserva').val(json.documentos);
            $('#id_monto_entrega_reserva').val(json.monto_entrega);
            $('#id_mesas_reserva').val(json.mesas);

            var options = '';
            for (var i=0;i < json.mesas.length;i++){
                options += '<option title="'+json.mesas[i].descripcion+'" value="'+json.mesas[i].id+'">'+json.mesas[i].descripcion+'</option>';
                $("#id_mesa_pedido_from option[value="+json.mesas[i].id+"]").remove();
            }
            $("#id_mesa_pedido_to").append(options);
            //set_total();
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

function set_total(){
    var total = 0;
    $('input[name$=-total_producto_pedido]').each(function (){
        total += this.value ? parseFloat(this.value) : 0;
    });

    //var linea_credito =  $('#id_linea_credito').val() || 0;
    //if (parseFloat(linea_credito) < total){
    //    alert('El Total de la Orden de Compra supera la Linea de Credito con el Proveedor.')
    //}
    $('#id_total_pedido').val(total);
}