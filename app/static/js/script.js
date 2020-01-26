$("#checkform").on("submit", (data) => {
  data.preventDefault()


  $.ajax("/check", {
    type: "POST",
    data: {code: $("#code").val()},
    cache: "false",
    dataType: "JSON",
    success: (data) => {
      if (Object.keys(data["result"]).length == 0) {
        $(".terminal").html("<p class=\"text-success\">Молодец!!!</p>")
        $("#next").show()
        } else {
            $.each(data, function(key, val){
            var str = ""
            str = str + val + "<br>"
            $(".terminal").html("<p class=\"text-danger\">" + str + "<br></p>")
        })
        }
        console.log(data)
    },
    error: (data) => {
     alert()
    }
  })


//  $.getJSON('http://127.0.0.1:5000/index/output.json', (data) => {
//
//
//
//
//  })
return false
})

window.onload = function() {

  setTimeout(function() {

    document.getElementById("preloader_malc").style.display = "none";

  }, 1000);

};
