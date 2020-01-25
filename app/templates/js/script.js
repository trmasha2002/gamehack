$.getJSON("/output.json", function(data) {
    console.log(JSON.parse(data));
});

window.onload = function() {

  setTimeout(function() {

    document.getElementById("preloader_malc").style.display = "none";

  }, 3000);

};
