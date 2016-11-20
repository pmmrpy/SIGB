/**
 * Created by pmmr on 29/10/2016.
 */
django.jQuery(document).ready(function(){

     $('#id_apertura_caja').change(function (){
         set_apertura_caja(this.value);
     });

    $('#id_rendicion_efectivo').keyup(function (){
        //var indice = this.name.split('-')[1];
        //var precio = $('#id_pedidodetalle_set-'+indice+'-precio_producto_pedido').val();
        var total_efectivo = $('#id_total_efectivo').val();
        var diferencia =  (total_efectivo? total_efectivo : 0) - ((this.value)? parseFloat(this.value) : 0);
        $('#id_diferencia_efectivo').val(diferencia);
        set_total_diferencia();
    });

    $('#id_rendicion_tcs').keyup(function (){
        //var indice = this.name.split('-')[1];
        //var precio = $('#id_pedidodetalle_set-'+indice+'-precio_producto_pedido').val();
        var total_tcs = $('#id_monto_registro_tcs').val();
        var diferencia =  (total_tcs? total_tcs : 0) - ((this.value)? parseFloat(this.value) : 0);
        $('#id_diferencia_tcs').val(diferencia);
        set_total_diferencia();
    });

    $('#id_rendicion_tds').keyup(function (){
        //var indice = this.name.split('-')[1];
        //var precio = $('#id_pedidodetalle_set-'+indice+'-precio_producto_pedido').val();
        var total_tds = $('#id_monto_registro_tds').val();
        var diferencia =  (total_tds? total_tds : 0) - ((this.value)? parseFloat(this.value) : 0);
        $('#id_diferencia_tds').val(diferencia);
        set_total_diferencia();
    });

    $('#id_rendicion_otros_medios').keyup(function (){
        //var indice = this.name.split('-')[1];
        //var precio = $('#id_pedidodetalle_set-'+indice+'-precio_producto_pedido').val();
        var total_om = $('#id_monto_registro_otros_medios').val();
        var diferencia =  (total_om? total_om : 0) - ((this.value)? parseFloat(this.value) : 0);
        $('#id_diferencia_otros_medios').val(diferencia);
        set_total_diferencia();
    });
});

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
    if (chosenId){
        set_apertura_caja(chosenId);
    //} else {
    //    set_producto_detalle(chosenId,name);
    }
}

function set_apertura_caja(id_apertura_caja) {
        $.ajax({
        url : "/ventas/get_apertura_caja/", // the endpoint
        type : "GET", // http method
        data : { id_apertura_caja : id_apertura_caja }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            //var indice = name.split('-')[1];
            //alert(JSON.stringify(json));

            $('#id_cajero').val(json.cajero);
            $('#id_caja').val(json.caja);
            $('#id_sector').val(json.sector);
            $('#id_horario').val(json.horario);
            $('#id_jornada').val(json.jornada);
            $('#id_fecha_hora_apertura_caja').val(json.fecha_hora_apertura_caja);
            $('#id_monto_apertura').val(json.monto_apertura);
            $('#id_estado_apertura_caja').val(json.estado_apertura_caja);
            $('#id_cantidad_total_operaciones_pendientes').val(json.cantidad_total_operaciones_pendientes);
            $('#id_cantidad_total_operaciones_canceladas').val(json.cantidad_total_operaciones_canceladas);
//==> Efectivo <==
            $('#id_cantidad_operaciones_efectivo_procesadas').val(json.cantidad_operaciones_efectivo_procesadas);
            $('#id_cantidad_operaciones_efectivo_pendientes').val(json.cantidad_operaciones_efectivo_pendientes);
            $('#id_cantidad_operaciones_efectivo_canceladas').val(json.cantidad_operaciones_efectivo_canceladas);
            $('#id_monto_registro_efectivo').val(json.monto_registro_efectivo);
            $('#id_total_efectivo').val(json.total_efectivo);
            $('#id_diferencia_efectivo').val(json.total_efectivo);
//==> TCs <==
            $('#id_cantidad_operaciones_tcs_procesadas').val(json.cantidad_operaciones_tcs_procesadas);
            $('#id_cantidad_operaciones_tcs_pendientes').val(json.cantidad_operaciones_tcs_pendientes);
            $('#id_cantidad_operaciones_tcs_canceladas').val(json.cantidad_operaciones_tcs_canceladas);
            $('#id_monto_registro_tcs').val(json.monto_registro_tcs);
            $('#id_diferencia_tcs').val(json.monto_registro_tcs);
//==> TDs <==
            $('#id_cantidad_operaciones_tds_procesadas').val(json.cantidad_operaciones_tds_procesadas);
            $('#id_cantidad_operaciones_tds_pendientes').val(json.cantidad_operaciones_tds_pendientes);
            $('#id_cantidad_operaciones_tds_canceladas').val(json.cantidad_operaciones_tds_canceladas);
            $('#id_monto_registro_tds').val(json.monto_registro_tds);
            $('#id_diferencia_tds').val(json.monto_registro_tds);
//==> Otros Medios de Pago <==
            $('#id_cantidad_operaciones_otros_medios_procesadas').val(json.cantidad_operaciones_otros_medios_procesadas);
            $('#id_cantidad_operaciones_otros_medios_pendientes').val(json.cantidad_operaciones_otros_medios_pendientes);
            $('#id_cantidad_operaciones_otros_medios_canceladas').val(json.cantidad_operaciones_otros_medios_canceladas);
            $('#id_monto_registro_otros_medios').val(json.monto_registro_otros_medios);
            $('#id_diferencia_otros_medios').val(json.monto_registro_otros_medios);
            set_total_diferencia();
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

function set_total_diferencia(){
    var total = 0;
    $('input[class="diferencia"]').each(function (){
        total += this.value ? parseFloat(this.value) : 0;
    });

    //var linea_credito =  $('#id_linea_credito').val() || 0;
    //if (parseFloat(linea_credito) < total){
    //    alert('El Total de la Orden de Compra supera la Linea de Credito con el Proveedor.')
    //}
    $('#id_total_diferencia').val(total);
}