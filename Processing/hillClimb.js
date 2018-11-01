var height, width
var img_h, img_w;
var img;

function preload(){
    img = loadImage('starry_night.jpg');
}

function setup(){

    height = img.height;
    width = img.width;
    createCanvas(width,height);
    background(255);
    ellipseMode(RADIUS);
    
}

var maxSize = 100;
var minSize = 2;
var alp = 255;

function draw(){
     
    img_w = img.width;
    img_h = img.height;
    if(maxSize!=minSize)
        rendertriangle()
        //renderellipse()
        //renderrect()

    if(frameCount%30 == 0){
        maxSize -= 2;
        maxSize = max(maxSize,minSize);
        alp--;
    }
}

function renderellipse(){

    for(var i = 0 ; i < width/maxSize ; ++i ){
        
        var x = floor(random(img_w));
        var y = floor(random(img_h));

        var radius = random(maxSize);

        var wi_off = random(-radius/2,radius/2);
        var hi_off = random(-radius/2,radius/2);

        var color = img.get(x,y);
        noStroke();
        fill(color[0], color[1], color[2], alp%128 + 128);
        ellipse(x,y,wi_off+radius,hi_off+radius);

    }
   
}

function renderrect(){
    for(var i = 0 ; i < width/maxSize ; ++i ){
        
        var x = floor(random(img_w));
        var y = floor(random(img_h));

        var radius = random(maxSize);

        var wi_off = random(-radius/2,radius/2);
        var hi_off = random(-radius/2,radius/2);

        var color = img.get(x,y);
        noStroke();
        fill(color[0], color[1], color[2], alp%128 + 128);
        rect(x,y,wi_off+radius,hi_off+radius);

    }


}

function rendertriangle(){
for(var i = 0 ; i < width/maxSize ; ++i ){
        
        var x1 = floor(random(img_w));
        var y1 = floor(random(img_h));

        var side_length = random(maxSize);

        var wi_off = random(-side_length,side_length);
        var hi_off = random(-side_length,side_length);
        var x2 = x1+wi_off
        var y2 = y1+hi_off

        var wi_off = random(-side_length,side_length);
        var hi_off = random(-side_length,side_length);
        var x3 = x2 + wi_off
        var y3 = y2 + hi_off
        
        var color = img.get((x1+x2+x3)/3,(y1+y2+y3)/3);
        noStroke();
        fill(color[0], color[1], color[2], alp%128 + 128);
        triangle(x1,y1,x2,y2,x3,y3);

    }
}