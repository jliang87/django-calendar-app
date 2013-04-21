$(document).on("click", ".close", function() {
    var id = $(this).data('id');
    $("#cell-"+id).popover('destroy');
});


$(document).on("click", ".erase", function(event) {
    event.preventDefault();
    var id = $(this).data('id');
    var pop = $('#cell-'+id).hasClass("left") ? "left" : "right" ;
    $("#formpop-"+id+" #id_form-0-DELETE").attr('checked', 'checked');
    $("#formpop-"+id).submit(
       $.ajax
        ({
            data: $("#formpop-"+id).serialize(), // get the form data
            type: "POST", // GET or POST
            url: $("#formpop-"+id).attr('action'), // the file to call
            success: function(data) { // on success..
                var cool = $(data);
                $('#cell-'+id).fadeOut(function()
                {
                    $(this).replaceWith(cool); 
                    $('#cell-'+id).fadeIn(900);
                });
                if (pop == "left")
                {
                    $('#cell-'+id).addClass("left");
                }
                else
                {
                    $('#cell-'+id).addClass("right");
                }
            }
        }),
        $("#td-"+id).data('filled', 'False'),
        $("#cell-"+id).popover('destroy')
   );
});


$(document).ready(function() {
    
    $.fn.do = function(obj, event) {
         var id = $(obj).data('id');
         var filled = $(obj).data('filled');
         var pop = $('#cell-'+id).hasClass("left") ? "left" : "right" ;
         var that = obj;
         if (filled == "False")
         {
           $("#form-"+id+" #id_form-0-snippet").attr("value", "30 min well spent!");
           $(that).data('filled', 'True');
           $("#form-"+id).submit(
               $.ajax
                ({
                    data: $("#form-"+id).serialize(), // get the form data
                    type: "POST", // GET or POST
                    url: $("#form-"+id).attr('action'), // the file to call
                    success: function(data) 
                    { // on success..
                        var cool = $(data);
                        $('#cell-'+id).replaceWith(cool);
                        $('#cell-'+id).fadeIn(800);
                        if (pop == "left")
                        {
                            $('#cell-'+id).addClass("left");
                        }
                        else
                        {
                            $('#cell-'+id).addClass("right");
                        }
                    }
                })
           );
         }
         else if (filled == "True")
         {
            if ( $("#cell-"+id).next('div.popover:visible').length === 0 ){
                if ( $("#cell-"+id).hasClass("left") )
                {
                    $("#cell-"+id).popover({placement:'left'}).popover('show');
                }
                else if ( $("#cell-"+id).hasClass("right") )
                {
                    $("#cell-"+id).popover({placement:'right'}).popover('show');
                }
            }
            $("#formpop-"+id).unbind('submit').on("submit", function(event){
                event.preventDefault();
                $.ajax
                ({
                    data: $("#formpop-"+id).serialize(), // get the form data
                    type: "POST", // GET or POST
                    url: $("#formpop-"+id).attr('action'), // the file to call
                    success: function(data) 
                    { // on success..
                        // $('#cell-'+id).stop(true, true);
                        var cool = $(data);
                        $('#cell-'+id).replaceWith(cool);
                        $('#cell-'+id).fadeIn(900);
                        if (pop == "left")
                        {
                            $('#cell-'+id).addClass("left");
                        }
                        else
                        {
                            $('#cell-'+id).addClass("right");
                        }
                    }
                });
                $("#cell-"+id).popover('destroy'); 
                return false;
            });
        }
    };

    
    $(".day, .current").on("click",function(event) {
         $(this).do(this, event);
    }); 
    
    $(".day").hover( 
        function() {
        var id = $(this).data('id');
        $(this).css( "background-color", "rgba(50,79,195,0.35)" );
        $('#edit-icon-'+id).stop(true, true).hide().css({
          visibility: "visible"
        }).fadeIn('slow');
        $('#pencil-icon-'+id).stop(true, true).hide().css({
          visibility: "visible"
        }).fadeIn('slow');
        $('#star-icon-'+id).css({ visibility: "hidden" });
        return this;
    }, function() {
        var id = $(this).data('id');
        $(this).css( "background-color", "rgba(50,79,195,0.4)" );
        $('#edit-icon-'+id).css({ visibility: "hidden" });
        $('#pencil-icon-'+id).css({ visibility: "hidden" });
        $('#star-icon-'+id).stop(true, true).hide().css({
          visibility: "visible"
        }).fadeIn('fast');
        return this;
      });
      
    $(".current").hover( 
        function() {
        var id = $(this).data('id');
        $('#edit-icon-'+id).stop(true, true).hide().css({
          visibility: "visible"
        }).fadeIn('slow');
        $('#pencil-icon-'+id).stop(true, true).hide().css({
          visibility: "visible"
        }).fadeIn('slow');
        $('#star-icon-'+id).css({ visibility: "hidden" });
        return this;
    }, function() {
        var id = $(this).data('id');
        $('#edit-icon-'+id).css({ visibility: "hidden" });
        $('#pencil-icon-'+id).css({ visibility: "hidden" });
        $('#star-icon-'+id).stop(true, true).hide().css({
          visibility: "visible"
        }).fadeIn('fast');
        return this;
      });
});
