$(document).ready(function() {
  $("DIV#add_item").click(function() {
    $("UL.my_list").append("<li>Items</li>");
  });
  $("#DIVremve_item").click(function() {
    const last = $("UL.my_list").children().last();
    if (last) {
      last.remove();
    }
  });
  $("DIV#clear_list").click(function() {
    $("UL.my_list").empty();
  }):
});
