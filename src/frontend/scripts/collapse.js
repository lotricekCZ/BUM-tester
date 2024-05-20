var coll = document.getElementsByClassName("collapsible");
var help = coll[0].nextElementSibling;
coll[0].addEventListener("click", function () {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    console.log("clicked");
    if (content.style.display === "block") {
        content.style.display = "none";
    } else {
        content.style.display = "block";
    }
});
coll[1].addEventListener("click", function () {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    console.log("clicked");
    if (content.style.display === "block") {
        content.style.display = "none";
    } else {
        content.style.display = "block";
    }
});
function hide(){
    if (help.style.display === "block") {
        help.style.display = "none";
    }
}
