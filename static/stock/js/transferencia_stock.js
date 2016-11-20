/**
 * Created by pmmr on 18/11/2016.
 */

django.jQuery(document).ready(function(){

    $('input[name$=-producto_transferencia]').change(function(){
        //alert(this.value + ' - ' + this.name);
        set_cant_existente_producto_por_deposito(this.value, this.name);
    });

    $(".field-unidad_medida select").attr("readonly", "readonly");
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

    //alert('name: ' + name + ' - chosenId: ' + chosenId);

    if (chosenId) {
        set_cant_existente_producto_por_deposito(chosenId, name);
    }
}

function set_cant_existente_producto_por_deposito(id_producto, name) {
    $.ajax({
        url : "/stock/get_cant_existente_producto_por_deposito/", // the endpoint
        type : "GET", // http method
        data : { id_producto : id_producto }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            var indice = name.split('-')[1];
            //alert(JSON.stringify(json));

            $('#lookup_id_transferenciastockdetalle_set-'+indice+'-producto_transferencia').next('strong').remove();
            $('#lookup_id_transferenciastockdetalle_set-'+indice+'-producto_transferencia').after('<strong>'+json.producto+'</strong>');

            $('#id_transferenciastockdetalle_set-'+indice+'-unidad_medida').val(json.unidad_medida_id);
            $('#id_transferenciastockdetalle_set-'+indice+'-cant_exist_dce').val(json.cant_exist_dce);
            $('#id_transferenciastockdetalle_set-'+indice+'-cant_exist_dbp').val(json.cant_exist_dbp);
            $('#id_transferenciastockdetalle_set-'+indice+'-cant_exist_dba').val(json.cant_exist_dba);
            $('#id_transferenciastockdetalle_set-'+indice+'-cant_exist_dco').val(json.cant_exist_dco);
            $('#id_transferenciastockdetalle_set-'+indice+'-cant_exist_dbi').val(json.cant_exist_dbi);
            $('#id_transferenciastockdetalle_set-'+indice+'-cant_total_existente').val(json.cant_existente);

        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}