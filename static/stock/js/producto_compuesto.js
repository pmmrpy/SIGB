/**
 * Created by pmmr on 28/08/2016.
 */

django.jQuery(document).ready(function(){

    $('#id_categoria').change(function(){
        $('#id_subcategoria').val('');
        $('#select2-id_subcategoria-container').html('');
    });

    $('input[name$=-cantidad_insumo]').keyup(function (){
        var indice = this.name.split('-')[1];
        var costo = $('#id_producto_cabecera-'+indice+'-costo_promedio_insumo').val();
        var total =  parseInt(((this.value)? parseFloat(this.value) : 0)*(costo? costo : 0));
        $('#id_producto_cabecera-'+indice+'-total_costo').val(total);
        set_total();
    });

    $('input[name=porcentaje_ganancia]').keyup(function (){
        set_precio_venta_sugerido();
    });

    $('input[type=checkbox]').on('change', function() {
        var suma = 0;
        $('input[type=checkbox]').each(function (key, value) {
            var indice = this.name.split('-')[1];
            var total_costo = $('#id_producto_cabecera-'+indice+'-total_costo').val();
            var a = $(value).is(':checked');
            if (a == false) {
                suma = suma + parseInt(total_costo)
            }
        });
        $('#id_costo_elaboracion').val(suma);
        set_precio_venta_sugerido();
    });

    DateTimeShortcuts.overrideTimeOptions = function () {
        var clockCount = 0;
        console.log('ready');
        $('ul.timelist').each(function () {
            var $this = $(this);
            var originalHref = $this.find('a').attr('href');
            console.log(originalHref);
            $this.find('li').remove();
            for (i=5; i <= 120; i+=5) {
                var newLink = '<li><a href="javascript:DateTimeShortcuts.handleClockQuicklink('+ clockCount + ', ' + i
                    + ');"> 00:'+ i +'</a></li>';
                $this.append(newLink);
            }
            //console.log($this.html());

            clockCount++;
        });
    };

    addEvent(window, 'load', DateTimeShortcuts.overrideTimeOptions);

    $(".field-unidad_medida_insumo select, .field-costo_promedio_insumo input, .field-total_costo input").attr("readonly", "readonly");

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
        set_insumo_producto_compuesto_detalle(chosenId,name);
    }

    //if (name == 'id_reserva'){
    //    set_reserva(chosenId);
    //} else {
    //    set_producto_detalle(chosenId,name);
    //}
}

function set_insumo_producto_compuesto_detalle(id_insumo,name) {
    $.ajax({
        url : "/stock/get_insumo_producto_compuesto_detalle/", // the endpoint
        type : "GET", // http method
        data : { id_insumo : id_insumo }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            var indice = name.split('-')[1];
            //alert(JSON.stringify(json));

            //alert($('#lookup_id_ordencompradetalle_set-'+indice+'-producto_orden_compra').());
            $('#lookup_id_producto_cabecera-'+indice+'-insumo').next('strong').remove();
            $('#lookup_id_producto_cabecera-'+indice+'-insumo').after('<strong>'+json.insumo+'</strong>');
            //var parent = $('#lookup_id_ordencompradetalle_set-'+indice+'-producto_orden_compra');
            //alert(JSON.stringify(parent.html()))

            $('#id_producto_cabecera-'+indice+'-unidad_medida_insumo').val(json.unidad_medida);
            $('#id_producto_cabecera-'+indice+'-costo_promedio_insumo').val(json.costo_promedio_insumo);
            $('#id_producto_cabecera-'+indice+'-cantidad_insumo').val('1');
            $('#id_producto_cabecera-'+indice+'-total_costo').val(json.costo_promedio_insumo);
            set_total();
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });

    //$(".field-unidad_medida_orden_compra select").attr("disabled", true);
}

function set_total(){
    var total = 0;
    $('input[name$=-total_costo]').each(function (){
        var indice = this.name.split('-')[1];
        //var a = $('#id_pedidodetalle_set-'+indice+'-cancelado').is(':checked');
        //alert(indice + ' - ' + a);

        if ($('#id_producto_cabecera-'+indice+'-DELETE').is(':checked') == false){
            total += this.value ? parseInt(this.value) : 0;
        }

    });

    $('#id_costo_elaboracion').val(total);
    set_precio_venta_sugerido();
}

function set_precio_venta_sugerido(){
    var porcentaje_ganancia = (($('#id_porcentaje_ganancia').val())? ($('#id_porcentaje_ganancia').val()) : 0);
    var costo_elaboracion = (($('#id_costo_elaboracion').val())? ($('#id_costo_elaboracion').val()) : 0);

    //if (parseFloat(porcentaje_ganancia) == 0){
    //    porcentaje_ganancia = 30;
    //    $('#id_porcentaje_ganancia').val(porcentaje_ganancia);
    //}

    var precio_venta_sugerido = parseInt((costo_elaboracion * porcentaje_ganancia) / 100) + parseInt(costo_elaboracion);

    //alert('Costo elaboracion: ' + costo_elaboracion + ' - Porc. Ganancia: ' + porcentaje_ganancia + ' - Precio Venta Sug: ' + precio_venta_sugerido);

    $('#id_precio_venta_sugerido').val(precio_venta_sugerido);
}