$(document).ready(function() {
  $("INPUT#language_code").keypress(function(event) {
    if (event.keycode === 13) {
      $("INPUT#btn_translate").click();
    };
  const = $("INPUT#language_code").val();
  $.get("https://www.fourtonfish.com/hellosalut/hello/'"+const+"'", function(data) {
    $("INPUT#btn_translate").click(function() {
      $("DIV#hello).text(const); 
  }); 
});
