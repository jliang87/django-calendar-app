$(document).ready(function() {
 // This is more like it!
     alert("sad");
     
     $(".day").hover( 
        function() {
        var id = $(this).data('id');
        $(this).css( "background-color", "rgba(245,200,200,0.3)" );
        $('.edit-icon-'+id).stop(true, true).hide().css({
          visibility: "visible"
        }).fadeIn("slow");
        return this;
    }, function() {
        var id = $(this).data('id');
        $(this).css( "background-color", "rgba(200,255,200,0.3)" );
        return $('.edit-icon-'+id).css({ visibility: "hidden" });
      });
      
    $(".current").hover( 
        function() {
        var id = $(this).data('id');
        $(this).css( "background-color", "rgba(245,200,200,0.3)" );
        $('.edit-icon-'+id).stop(true, true).hide().css({
          visibility: "visible"
        }).fadeIn("slow");
        return this;
    }, function() {
        var id = $(this).data('id');
        $(this).css( "background-color", "rgba(200,200,255,0.5)" );
        return $('.edit-icon-'+id).css({ visibility: "hidden" });
      });
});
