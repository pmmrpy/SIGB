/**
 * Created by pmmr on 10/11/2016.
 */
django.jQuery(document).ready(function(){

     $('#id_cliente').change(function (){
         set_cliente(this.value);
     });

    DateTimeShortcuts.overrideTimeOptions = function () {
        var clockCount = 0;
        console.log('ready');
        $('ul.timelist').each(function () {
            var $this = $(this);
            var originalHref = $this.find('a').attr('href');
            console.log(originalHref);
            $this.find('li').remove();
            for (i=18; i <= 21; i++) {
                var newLink = '<li><a href="javascript:DateTimeShortcuts.handleClockQuicklink('+ clockCount + ', ' + i
                    + ');"> ' + i + ':00h</a></li>';
                $this.append(newLink);
            }
            //console.log($this.html());

            clockCount++;
        });
    };

    addEvent(window, 'load', DateTimeShortcuts.overrideTimeOptions);

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

    if (name == 'id_cliente'){
        set_cliente(chosenId);
    }
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

            $('#lookup_id_cliente').next('strong').remove();
            $('#lookup_id_cliente').after().after('<strong>'+json.cliente.nombre_cliente+'</strong>');

            var options = '';
            $("#id_cliente_documento_reserva option").remove();
            //$("#id_documento_cliente").append(options);
            for (var i=0;i < json.documentos.length;i++){
                if (json.documentos[i].t_doc == 'RUC') {
                    //options += '<option title="'+json.documentos[i].t_doc+'" value="'+json.documentos[i].num_doc+'-'+json.documentos[i].dv+'">'+json.documentos[i].t_doc+': '+json.documentos[i].num_doc+'-'+json.documentos[i].dv+'</option>';
                    options += '<option title="'+json.documentos[i].t_doc+'" value="'+json.documentos[i].t_doc+': '+json.documentos[i].num_doc+'-'+json.documentos[i].dv+'">'+json.documentos[i].t_doc+': '+json.documentos[i].num_doc+'-'+json.documentos[i].dv+'</option>';
                } else {
                    //options += '<option title="'+json.documentos[i].t_doc+'" value="'+json.documentos[i].num_doc+'">'+json.documentos[i].t_doc+': '+json.documentos[i].num_doc+'</option>';
                    options += '<option title="'+json.documentos[i].t_doc+'" value="'+json.documentos[i].t_doc+': '+json.documentos[i].num_doc+'">'+json.documentos[i].t_doc+': '+json.documentos[i].num_doc+'</option>';
                }
            }
            $("#id_cliente_documento_reserva").append(options);

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