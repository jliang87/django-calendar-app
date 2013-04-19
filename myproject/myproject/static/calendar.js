$(document).ready(function() {
     $(".day, .current").click(function() {
         var id = $(this).data('id');
         var filled = $(this).data('filled');
         if (filled == "False")
         {
           $("#form-"+id+" #id_form-0-snippet").attr("value", "30 min well spent!");
           $("#form-"+id).submit(
               $.ajax
                ({
                    data: $("#form-"+id).serialize(), // get the form data
                    type: "POST", // GET or POST
                    url: $("#form-"+id).attr('action'), // the file to call
                    success: function(data) { // on success..
                     var cool = $(data);
                     $('#try').replaceWith(cool);
                     }
                })
           );
         }
         else if (filled == "True")
         {
            $("#form-"+id+" #id_form-0-DELETE").attr('checked','checked');
            $("#form-"+id).submit(
             $.ajax
                ({
                    data: $("#form-"+id).serialize(), // get the form data
                    type: "POST", // GET or POST
                    url: $("#form-"+id).attr('action'), // the file to call
                    success: function(data) { // on success..
                     var cool = $(data);
                     $('#try').replaceWith(cool);
                     }
                })    
            );
         }
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
