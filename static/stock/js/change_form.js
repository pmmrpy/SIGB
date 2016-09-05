/**
 * Created by pmmr on 28/08/2016.
 */

django.jQuery(document).ready(function(){
    $('#id_categoria').change(function(){
        $('#id_subcategoria').val('');
        $('#select2-id_subcategoria-container').html('');
    });
});