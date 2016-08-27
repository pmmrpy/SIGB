/**
 * Created by pmmr on 23/08/2016.
 */

django.jQuery(document).ready(function(){


    $('.auto').autoNumeric('init', {aSign: '  GS', pSign: 's', mDec:0});
    alert('Entra a change_form.js')

});
django.jQuery(document).on('formset:removed', function(event, $row, formsetName) {
   //setAll();
    alert('probando eliminar');
});
django.jQuery(document).on('formset:added', function(event, $row, formsetName) {
   alert('probando');
});