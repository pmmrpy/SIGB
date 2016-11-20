/**
 * Created by pmmr on 07/10/2016.
 */
django.jQuery(document).ready(function(){
//(function($) {
//    $(document).ready(function() {

    $('input[name$=-cantidad_producto_venta]').keyup(function (){
        var indice = this.name.split('-')[1];
        var precio = $('#id_ventaocasionaldetalle_set-'+indice+'-precio_producto_venta').val();
        var total =  ((this.value)? parseFloat(this.value) : 0)*(precio? precio : 0);
        $('#id_ventaocasionaldetalle_set-'+indice+'-total_producto_venta').val(total);
        set_total();
    });

     $('#id_cliente_factura').change(function (){
         set_cliente(this.value);
     });

    $('#id_efectivo_recibido').keyup(function (){
        var total_venta = $('#id_total_venta').val();
        var vuelto = ((this.value)? parseFloat(this.value) : 0) - (total_venta? total_venta : 0);
        $('#id_vuelto').val(vuelto);
        //set_total_diferencia();
    });

    //if (document.getElementById("id_forma_pago").value == ''){
    //    $('#id_efectivo_recibido').prop('readonly', true).val(0);
    //    $('#id_voucher').prop('readonly', true).val();
    //    $('#id_vuelto').val(0);
    //}else if (document.getElementById("id_forma_pago").value == 'EF'){
    //    $('#id_efectivo_recibido').removeAttr('readonly');
    //    $('#id_voucher').prop('readonly', true).val();
    //    $('#id_vuelto').val(0);
    //}else if (document.getElementById("id_forma_pago").value == 'OM'){
    //    $('#id_efectivo_recibido').removeAttr('readonly');
    //    $('#id_voucher').prop('readonly', true).val();
    //    $('#id_vuelto').val(0);
    //}else if (document.getElementById("id_forma_pago").value == 'TD'){
    //    $('#id_efectivo_recibido').prop('readonly', true).val(0);
    //    $('#id_voucher').removeAttr('readonly');
    //    $('#id_vuelto').val(0);
    //}else if (document.getElementById("id_forma_pago").value == 'TC'){
    //    $('#id_efectivo_recibido').prop('readonly', true).val(0);
    //    $('#id_voucher').removeAttr('readonly');
    //    $('#id_vuelto').val(0);
    //}

    $("#id_forma_pago").change(function(){
      if (this.value == 'EF') {
          $('#id_efectivo_recibido').removeAttr('readonly');
          $('#id_voucher').prop('readonly', true).val('');
          $('#id_vuelto').val(0);
      }else if (this.value == 'OM'){
        $('#id_efectivo_recibido').removeAttr('readonly');
        $('#id_voucher').prop('readonly', true).val('');
        $('#id_vuelto').val(0);
      }else if (this.value == 'TD'){
        $('#id_efectivo_recibido').prop('readonly', true).val(0);
        $('#id_voucher').removeAttr('readonly');
        $('#id_vuelto').val(0);
      }else if (this.value == 'TC'){
        $('#id_efectivo_recibido').prop('readonly', true).val(0);
        $('#id_voucher').removeAttr('readonly');
        $('#id_vuelto').val(0);
      }else if (this.value == ''){
        $('#id_efectivo_recibido').prop('readonly', true).val(0);
        $('#id_voucher').prop('readonly', true).val('');
        $('#id_vuelto').val(0);
      }
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
            var total_producto = $('#id_ventaocasionaldetalle_set-'+indice+'-total_producto_venta').val();
            var a = $(value).is(':checked');
            if (a == false) {
                suma = suma + parseFloat(total_producto)
            }
        });
        $('#id_total_venta').val(suma);
    });

    $(".field-precio_producto_venta input, .field-total_producto_venta input").attr("readonly", "readonly");
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

    //if (chosenId){
    //   set_producto_detalle(chosenId,name);
    //}

    if (name == 'id_cliente_factura'){
        set_cliente(chosenId);
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

            $('#id_ventaocasionaldetalle_set-'+indice+'-precio_producto_venta').val(json.precio_venta);
            $('#id_ventaocasionaldetalle_set-'+indice+'-cantidad_producto_venta').val('1');
            $('#id_ventaocasionaldetalle_set-'+indice+'-total_producto_venta').val(json.precio_venta);
            set_total();

            //alert($('#lookup_id_ordencompradetalle_set-'+indice+'-producto_orden_compra').());
            $('#lookup_id_ventaocasionaldetalle_set-'+indice+'-producto_venta').next('strong').remove();
            $('#lookup_id_ventaocasionaldetalle_set-'+indice+'-producto_venta').after('<strong>'+json.producto+'</strong>');
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

function set_cliente(id_cliente) {
    $.ajax({
        url : "/ventas/get_cliente/", // the endpoint
        type : "GET", // http method
        data : { id_cliente : id_cliente }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            //var indice = name.split('-')[1];
            //alert(JSON.stringify(json));

            //$('#id_id_cliente_reserva').val(json.cliente.id);
            //$('#id_cliente_reserva').val(json.cliente.nombre_cliente);
            //$('#id_documentos_cliente').val(json.documentos);

            // ---> Consultar con JUANBER como limpiar el texto de este selector antes de asignar el nuevo valor
            //$('#lookup_id_cliente_factura').after().remove();
            $('#lookup_id_cliente_factura').next('strong').remove();
            $('#lookup_id_cliente_factura').after().after('<strong>'+json.cliente.nombre_cliente+'</strong>');

            var options = '';
            $("#id_cliente_documento_factura option").remove();
            //$("#id_cliente_documento_factura").append(options);
            for (var i=0;i < json.documentos.length;i++){
                if (json.documentos[i].t_doc == 'RUC') {
                    options += '<option title="'+json.documentos[i].t_doc+'" value="'+json.documentos[i].t_doc+': '+json.documentos[i].num_doc+'-'+json.documentos[i].dv+'">'+json.documentos[i].t_doc+': '+json.documentos[i].num_doc+'-'+json.documentos[i].dv+'</option>';
                } else {
                    options += '<option title="'+json.documentos[i].t_doc+'" value="'+json.documentos[i].t_doc+': '+json.documentos[i].num_doc+'">'+json.documentos[i].t_doc+': '+json.documentos[i].num_doc+'</option>';
                }
            }
            $("#id_cliente_documento_factura").append(options);

            $('#id_direccion_cliente').val(json.direccion);
            $('#id_pais_cliente').val(json.pais);
            $('#id_ciudad_cliente').val(json.ciudad);
            $('#id_telefonos_cliente').val(json.telefonos);
            $('#id_email').val(json.email);

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
    $('input[name$=-total_producto_venta]').each(function (){
        total += this.value ? parseFloat(this.value) : 0;
    });

    //var linea_credito =  $('#id_linea_credito').val() || 0;
    //if (parseFloat(linea_credito) < total){
    //    alert('El Total de la Orden de Compra supera la Linea de Credito con el Proveedor.')
    //}
    $('#id_total_venta').val(total);
    $('#id_efectivo_recibido').val(0);
    $('#id_vuelto').val(0);
    $('#id_voucher').val('');
}