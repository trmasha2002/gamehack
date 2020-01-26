$("#apply").on("click", (e) => {
  e.preventDefault()
  $.ajaxSetup({ cache: false });

  $.getJSON('http://127.0.0.1:5000/index.html/output.json', (data) => {


    var str = ""

    if (Object.keys(data["0"]).length == 0) {
      $(".terminal").html("<p class=\"text-success\">Молодец!!!</p>")
      $("#next").show()
    } else {
      $.each(data["0"], function(key, val){
        str = str + val + "<br>"
        $(".terminal").html("<p class=\"text-danger\">" + str + "</p>")
      })
    }
  })
})

window.onload = function() {

  setTimeout(function() {

    document.getElementById("preloader_malc").style.display = "none";

  }, 1000);

};
