/**
 * Created by pmmr on 23/08/2016.
 */

django.jQuery(document).ready(function(){

    //$("#id_linea_credito").mask('#.##0', {reverse: true});
    //$("#id_total_orden_compra").mask('#.##0');

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

     $('#id_proveedor_orden_compra').change(function (){
         set_linea_credito(this.value);
     });

    $('input[type=checkbox]').on('change', function() {
        var suma = 0;
        $('input[type=checkbox]').each(function (key, value) {
            var a = $(value).is(':checked');
            if (a == false) {
                suma = suma + parseFloat(value.parentElement.parentElement.children[3].children[0].value)
            }
        });
        $('#id_total_orden_compra').val(suma);
    });

    // Cuando se elimina un item del inline se debe actualizar el Total de la Orden de Compra
    $('.inline-deletelink').click(function (){
        set_total();
    });

    // https://docs.djangoproject.com/es/1.10/ref/contrib/admin/javascript/
    $(document).on('formset:removed', function(event, $row, formsetName) {
        // Row removed
        set_total();
    });

    //$(".field-total_producto_orden_compra input, .field-unidad_medida_orden_compra input, .field-total_orden_compra input").attr("readonly", "readonly");
    //$(".field-unidad_medida_orden_compra select").attr("disabled", true);
    $(".field-unidad_medida_orden_compra select").attr("readonly", true);
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
         set_producto_detalle(chosenId,name);
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

            $('#id_ordencompradetalle_set-'+indice+'-precio_producto_orden_compra').val(json.precio_compra);
            //$(".field-unidad_medida_orden_compra select").attr("disabled", false);
            $('#id_ordencompradetalle_set-'+indice+'-unidad_medida_orden_compra').val(json.unidad_medida_producto_id);
            //$('#id_ordencompradetalle_set-'+indice+'-unidad_medida_orden_compra').val(json.unidad_medida_producto_display);
            $('#id_ordencompradetalle_set-'+indice+'-cantidad_producto_orden_compra').val('1');
            $('#id_ordencompradetalle_set-'+indice+'-total_producto_orden_compra').val(json.precio_compra);
            set_total();

            //alert($('#lookup_id_ordencompradetalle_set-'+indice+'-producto_orden_compra').());
//)
            $('#lookup_id_ordencompradetalle_set-'+indice+'-producto_orden_compra').after('<strong>'+json.producto+'</strong>');
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

function set_linea_credito(id_proveedor) {
    $.ajax({
        url : "/compras/get_linea_credito/", // the endpoint
        type : "GET", // http method
        data : { id_proveedor : id_proveedor }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#id_linea_credito').val(json.linea_credito);
        },
        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            $('#id_linea_credito').val('0');
        }
    });
}

function set_total(){
    var total = 0;
    $('input[name$=-total_producto_orden_compra]').each(function (){
        total += this.value ? parseFloat(this.value) : 0;
    });

    var linea_credito =  $('#id_linea_credito').val() || 0;
    if (parseFloat(linea_credito) < total){
        alert('El Total de la Orden de Compra supera la Linea de Credito con el Proveedor.')
    }
    $('#id_total_orden_compra').val(total);
}
