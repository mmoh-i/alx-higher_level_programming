$(document).ready(function() {
  $.getJSON("https://swapi-api.hbtn.io/api/films/?format=json", function(data) {
    $("#list_movies").append("<li>'" + data.title + "'</li>");
  });
});
