$(document).ready(function() {
 // This is more like it!
     alert("sad");
     $("td").hover( 
        function() {
        var id = $(this).data('id');
        $('.edit-icon-'+id).stop(true, true).hide().css({
          visibility: "visible"
        }).fadeIn("slow");
        return this;
    }, function() {
         var id = $(this).data('id');
        return $('.edit-icon-'+id).fadeOut("fast", function() {
        return $('.edit-icon-'+id).show().css({ visibility: "hidden" });
      });
    });
});
