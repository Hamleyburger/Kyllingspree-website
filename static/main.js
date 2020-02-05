


/* MAKE KYLLING WAG ON HOVER */
$(function()
{
    $("#mylogo").hover(
        function() {
            $(this).attr("src", "/static/src/navimgs/Kyllogo.gif");
        },
        function() {
            $(this).attr("src", "/static/src/navimgs/Kyllogo.png");
        }
    );
});


function changeImg(){
var myimg = document.getElementById("randombanner");
var imgarray = ["/static/src/ads/hotdogsad.gif", "/static/src/ads/buysausage.gif", "/static/src/ads/dogfood.jpeg", "/static/src/ads/nonormalgame.png", "/static/src/ads/sharpteeth.png"];
var imgindex = Math.floor(Math.random() * imgarray.length);
console.log(imgindex);

    myimg.setAttribute("src", imgarray[imgindex]);

}

function formAlert() {
  alert("Apologies! Kylling is currently closed to new requests.");
}

changeImg();

