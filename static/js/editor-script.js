var example = document.getElementById("Canvas"),
ctx = example.getContext('2d');
example.height = 750;
example.width  = 650;
Img0 = new Image();Img0.src = '/static/img/start.png';
Img0.onload= function(){
ctx.drawImage(Img0, 275, 50);
}
Img1 = new Image();Img1.src = '/static/img/condition.png';
Img1.onload= function(){
ctx.drawImage(Img1, 275, 140);
}
Img2 = new Image();Img2.src = '/static/img/declar.png';
Img2.onload= function(){
ctx.drawImage(Img2, 185, 230);
}
Img3 = new Image();Img3.src = '/static/img/declar.png';
Img3.onload= function(){
ctx.drawImage(Img3, 365, 230);
}
Img4 = new Image();Img4.src = '/static/img/input.png';
Img4.onload= function(){
ctx.drawImage(Img4, 275, 320);
}
Img5 = new Image();Img5.src = '/static/img/end.png';
Img5.onload= function(){
ctx.drawImage(Img5, 275, 410);
}
