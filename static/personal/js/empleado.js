/**
 * Created by pmmr on 28/08/2016.
 */

django.jQuery(document).ready(function(){
    $('#id_pais').change(function(){
        $('#id_ciudad').val('');
        $('#select2-id_ciudad-container').html('');
    });

    //Limpiar "Codigo de Operadora - Telefono" cuando cambia "Codigo de Pais - Telefono"
    $('#select2-id_empleadotelefono_set-0-codigo_pais_telefono-container').change(function(){
        $('#id_empleadotelefono_set-0-codigo_operadora_telefono').val('');
        $('#select2-id_empleadotelefono_set-0-codigo_operadora_telefono-container').html('');
    });
});