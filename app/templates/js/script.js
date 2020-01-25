$("#apply").on("click", (e) => {
  e.preventDefault()

  $.getJSON('http://вот здесь напиши адрес своего сервака/output.json', function(data){

    var str = ""


      $.each(data["0"], function(key, val){
        str = str + val;
        $(".terminal").html("<p class=\"text-danger\">" + str + "</p>")
      })
  })
})

window.onload = function() {

  setTimeout(function() {

    document.getElementById("preloader_malc").style.display = "none";

  }, 1000);

};
