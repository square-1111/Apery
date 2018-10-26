var height, width
var img_h, img_w;
var img;

function setup(){

    height = window.innerHeight;
    width = window.innerWidth;
    createCanvas(width,height);
    background(255);
    
    ellipseMode(RADIUS);
    
    img =  loadImage('hoovertowernight.jpg');

    
    
}

var maxSize = 80;
var minSize = 5;

function draw(){
    frameRate(200);
    
    img_w = img.width;
    img_h = img.height;
    
    for(var i = 0 ; i < width/maxSize ; ++i ){
        
        var x = floor(random(img_w));
        var y = floor(random(img_h));

        var radius = random(maxSize);

        var wi_off = random(-radius/2,radius/2);
        var hi_off = random(-radius/2,radius/2);

        var color = img.get(x,y);

        fill(color, 127);
        noStroke();

        console.log(color);

        ellipse(x,y,wi_off+radius,hi_off+radius);

    }
    if(frameCount%30 == 0){
        maxSize -= 2;
        maxSize = max(maxSize,minSize);
    }

    
    // image(img, (width-img_w)/2, (height-img_h)/2);
}