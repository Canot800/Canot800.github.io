    $(function() {

        $('#colorselector').change(function(){
             $('.photo').hide();

            $("div[id^='"+$(this).val()+"']").show();



        });
    });