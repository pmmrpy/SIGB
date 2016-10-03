/**
 * Created by pmmr on 25/05/2016.
 */

//(function($) {
//    $(document).ready(function() {
// })(django.jQuery);

django.jQuery(document).ready(function(){

    //$('select[name$=-unidad_medida_compra]').each(function (){
    //    this.disabled = 'disabled'
    //});
    console.log($.fn.jquery);

    //Prueba de Masked Input Plugin

    var options =  {
        onInvalid: function(val, e, f, invalid, options){
            var error = invalid[0];
            $("#id_numero_factura_compra").val('')
        },
        placeholder: "___-___-_______", clearIfNotMatch: true
    };

    $("#id_numero_factura_compra").mask('000-000-0000000', options);
    //$("#id_numero_factura_compra").mask("999-999-9999999",{completed:function(){alert("Ejecutado el mask: "+this.val());}});
    //$("#product").mask("99/99/9999",{completed:function(){alert("You typed the following: "+this.val());}});
    //$("#id_disponible_linea_credito_proveedor").mask('#.##0', {reverse: true});
    //$("#id_total_compra").mask('#.##0', {reverse: true});

    $("#id_nro_orden_compra").change(function (event) {
    //$("#id_numero_orden_compra").change(function (event) {
        var boton = $('#compra_form button[name="_continue"]');
        //boton.val('cambio_nro_orden')
        //$("#id_numero_orden_compra").val(this.value);
        //var numero_orden_compra = $("#id_numero_orden_compra").val();
        //var numero_orden_compra = this.value;
        //alert('nro_orden_compra: ' + numero_orden_compra);
        boton.click();
        //var proveedor = $('#id_compradetalle_set-'+indice+'-precio_producto_compra').val();
        //set_linea_credito(proveedor);
        //alert('Finaliza boton.click');
        //set_orden_compra(this.value);
    });

    //$(".field-precio_producto_compra input, .field-cantidad_producto_compra input").blur(function (event) {
    //    var valor = $(event.target);
    //    var columna = valor.parent();
    //    var fila = columna.parent();
    //
    //    var total_producto = $('.field-total_producto_compra input', fila);
    //    var precio_producto = $('.field-precio_producto_compra input', fila);
    //    var cantidad_producto = $('.field-cantidad_producto_compra input', fila);
    //    var total_compra = $('#id_total_compra');
    //    total_producto.val(precio_producto.val() * cantidad_producto.val());
    //    var suma = 0;
    //    var totales = $(".field-total_producto_compra input");
    //
    //    for (var i = 0; i < totales.length; i++) {
    //        suma += parseFloat($(totales[i]).val());
    //    }
    //    total_compra.val(suma);
    //});

    $('input[name$=-precio_producto_compra]').keyup(function (){
        var indice = this.name.split('-')[1];
        var cantidad = $('#id_compradetalle_set-'+indice+'-cantidad_producto_compra').val();
        var total =  ((this.value)? parseFloat(this.value) : 0)*(cantidad? cantidad : 0);
        $('#id_compradetalle_set-'+indice+'-total_producto_compra').val(total)
        set_total();
    });

    $('input[name$=-cantidad_producto_compra]').keyup(function (){
        var indice = this.name.split('-')[1];
        var precio = $('#id_compradetalle_set-'+indice+'-precio_producto_compra').val();
        var total =  ((this.value)? parseFloat(this.value) : 0)*(precio? precio : 0);
        $('#id_compradetalle_set-'+indice+'-total_producto_compra').val(total)
        set_total();
    });

    $('input[type=checkbox]').on('change', function() {
        var suma = 0;
        $('input[type=checkbox]').each(function (key, value) {
            var a = $(value).is(':checked');
            if (a == false) {
                suma = suma + parseFloat(value.parentElement.parentElement.children[3].children[0].value)
            }
        });
        $('#id_total_compra').val(suma);
    });

    //$(".field-total_producto_compra input, .field-total_compra input").attr("readonly", "readonly");
    //$(".field-unidad_medida_compra select").attr("readonly", true);
    $('#id_numero_orden_compra').attr("readonly", true);
    //$('#id_numero_orden_compra').attr("disabled", true);

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
    if (chosenId)
         set_producto_detalle(chosenId, name);
}

function set_orden_compra(id_orden_compra) {
        $.ajax({
        url : "/compras/get_orden_compra/", // the endpoint
        type : "GET", // http method
        data : { id_orden_compra : id_orden_compra }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            //var indice = name.split('-')[1];
            //alert(JSON.stringify(json));

            //$('#id_proveedor').val(json.proveedor.id);
            $('#id_linea_credito').val(json.linea_credito);
            //set_total();
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}


function set_producto_detalle(id_producto,name) {
    $.ajax({
        url : "/stock/get_producto_detalle/", // the endpoint
        type : "GET", // http method
        data : { id_producto : id_producto }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            var indice = name.split('-')[1];
            //alert(JSON.stringify(json));

            //$('#id_linea_credito').val(json.linea_credito);
            $('#id_compradetalle_set-'+indice+'-precio_producto_compra').val(json.precio_compra);
            //$(".field-unidad_medida_compra select").attr("disabled", false);
            $('#id_compradetalle_set-'+indice+'-unidad_medida_compra').val(json.unidad_medida_producto_id);
            //$('#id_compradetalle_set-'+indice+'-unidad_medida_compra').val(json.unidad_medida_producto_display);
            $('#id_compradetalle_set-'+indice+'-cantidad_producto_compra').val('1');
            $('#id_compradetalle_set-'+indice+'-total_producto_compra').val(json.precio_compra);
            set_total();

            //alert($('#lookup_id_ordencompradetalle_set-'+indice+'-producto_orden_compra').());
//)
            $('#lookup_id_compradetalle_set-'+indice+'-producto_compra').after('<strong>'+json.producto+'</strong>');
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

//function set_linea_credito(id_proveedor) {
//    $.ajax({
//        url : "/compras/get_linea_credito/", // the endpoint
//        type : "GET", // http method
//        data : { id_proveedor : id_proveedor }, // data sent with the post request
//
//        // handle a successful response
//        success : function(json) {
//            $('#id_linea_credito').val(json.linea_credito);
//        },
//        // handle a non-successful response
//        error : function(xhr,errmsg,err) {
//            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
//            $('#id_linea_credito').val('0');
//        }
//    });
//}

function set_total(){
    var total = 0;
    $('input[name$=-total_producto_compra]').each(function (){
        total += this.value ? parseFloat(this.value) : 0;
    });

    var linea_credito =  $('#id_disponible_linea_credito_proveedor').val() || 0;
    if (parseFloat(linea_credito) < total){
        alert('El Total de la Compra supera la Linea de Credito con el Proveedor.')
    }
    $('#id_total_compra').val(total);
}
