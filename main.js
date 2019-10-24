


/* MAKE KYLLING WAG ON HOVER */
$(function()
{
    $("#mylogo").hover(
        function() {
            $(this).attr("src", "src/navimgs/Kyllogo.gif");
        },
        function() {
            $(this).attr("src", "src/navimgs/Kyllogo.png");
        }
    );
});


function changeImg(){
var myimg = document.getElementById("randombanner");
var imgarray = ["src/ads/buysausage.gif", "src/ads/hotdogsad.gif", "src/ads/dogfood.jpeg", "src/ads/nonormalgame.png", "src/ads/sharpteeth.png"];
var imgindex = Math.floor(Math.random() * imgarray.length);
console.log(imgindex);

    myimg.setAttribute("src", imgarray[imgindex]);

}

changeImg();
                    
