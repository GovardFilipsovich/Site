var example = document.getElementById("Canvas"),
ctx = example.getContext('2d');
example.height = 750;
example.width  = 650;
Img0 = new Image();Img0.src = '/static/img/start.png';
Img0.onload= function(){
ctx.drawImage(Img0, 50, 50);
}
Img1 = new Image();Img1.src = '/static/img/start.png';
Img1.onload= function(){
ctx.drawImage(Img1, 50, 50);
}
