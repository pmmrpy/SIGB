/**
 * Created by pmmr on 27/08/2016.
 */

django.jQuery(document).ready(function(){
    $('#id_pais').change(function(){
        $('#id_ciudad').val('');
        $('#select2-id_ciudad-container').html('');
    });
});