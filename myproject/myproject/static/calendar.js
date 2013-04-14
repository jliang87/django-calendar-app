$.fn.showEdit = function(id) {
  $(document).on('click', '#pencil-'+id, (function(event) { $('#td-'+id).css("overflow", "visible"); $(this).popover('show', {html:'true'}); event.preventDefault(); }));
};

$.fn.hideEdit = function(id) {
  $('#td-'+id).css("overflow-y", "scroll");
  $('#pencil-'+id).popover('destroy', {html:'false'});
};

$(document).ready(function() {
     $(".day").hover( 
        function() {
        var id = $(this).data('id');
        $(this).css( "background-color", "rgba(200,255,200,0.25)" );
        $(this).showEdit(id);
        $('.edit-icon-'+id).stop(true, true).hide().css({
          visibility: "visible"
        }).fadeIn('slow');
        $('.pencil-icon-'+id).stop(true, true).hide().css({
          visibility: "visible"
        }).fadeIn('slow');
        return this;
    }, function() {
        var id = $(this).data('id');
        $(this).hideEdit(id);
        $(this).css( "background-color", "rgba(200,255,200,0.3)" );
        $('.edit-icon-'+id).css({ visibility: "hidden" });
        $('.pencil-icon-'+id).css({ visibility: "hidden" });
        return this;
      });
      
    $(".current").hover( 
        function() {
        var id = $(this).data('id');
        $(this).css( "background-color", "rgba(200,200,255,0.45)" );
        $('.edit-icon-'+id).stop(true, true).hide().css({
          visibility: "visible"
        }).fadeIn('slow');
         $('.pencil-icon-'+id).stop(true, true).hide().css({
          visibility: "visible"
        }).fadeIn('slow');
        return this;
    }, function() {
        var id = $(this).data('id');
        $(this).css( "background-color", "rgba(200,200,255,0.5)" );
        $('.edit-icon-'+id).css({ visibility: "hidden" });
        $('.pencil-icon-'+id).css({ visibility: "hidden" });
        return this;
      });
});
