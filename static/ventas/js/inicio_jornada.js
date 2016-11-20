/**
 * Created by pmmr on 29/10/2016.
 */
django.jQuery(document).ready(function(){

    $('.vDateField').each(function(){
        $(this).removeProp('class').prop('readonly','readonly').css({'width':'80px'});
    });

    $('.vTimeField').each(function (){
         $(this).removeProp('class').prop('readonly','readonly').css({'width':'80px'});
    });

});