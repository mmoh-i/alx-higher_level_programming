$(document).ready(function(){
  $("#toggle_header").click(function(){
    var chng = $('header').css("color");
    if (chng == "green"){
      $('header').css('color', "red");
    }
    else
    {
      $('header').css('color', "green");
    }
  });
});

