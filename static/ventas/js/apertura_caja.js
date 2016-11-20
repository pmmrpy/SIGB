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
    //var elements = document.getElementsByClassName('datetimeshortcuts');
    //alert(elements);



    //DateTimeShortcuts.hide();

    //$('input[name$=-id]').each(function (){
    //    if(this.value){
    //        var id = this.id.split('-')[1];
    //        $(`a[id=lookup_id_pedidodetalle_set-${id}-producto_pedido]`).css({'display':'none'});
    //    }
    //});

    //DateTimeShortcuts.overrideTimeOptions = function () {
    //    var clockCount = 0;
    //    console.log('ready');
    //    $('ul.timelist').each(function () {
    //        var $this = $(this);
    //        var originalHref = $this.find('a').attr('href');
    //        console.log(originalHref);
    //        $this.find('li').remove();
    //        for (i=8; i <= 20; i++) {
    //            var newLink = '<li><a href="javascript:DateTimeShortcuts.handleClockQuicklink('+ clockCount + ', ' + i
    //                + ');"> ' + i + ':00h</a></li>';
    //            $this.append(newLink);
    //        }
    //        //console.log($this.html());
    //
    //        clockCount++;
    //    });
    //};
    //
    //addEvent(window, 'load', DateTimeShortcuts.overrideTimeOptions);
});