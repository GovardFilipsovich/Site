var example = document.getElementById("Canvas"),
ctx = example.getContext('2d');
example.height = 750;
example.width  = 650;
Img = new Image();Img.src = '/static/img/function.png';
Img.onload = function() {
ctx.drawImage(Img,50, 50);
}
