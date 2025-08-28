function setup() {
    createCanvas(400, 400);
  }
  
  function draw() {
    background(220);
    frogEyes(200, 200, 50);
    
}

function frogEyes(x, y, d) {
    eye(x - d/2, y, 50, 200, 5, false);
    eye(x + d/2, y, 50, 200, 5, keyIsPressed);
}

function eye(x, y, d, fc/*fillcolor*/, thickness, wink) {
    stroke(fc - 70);
    strokeWeight(thickness);
    fill(fc);
    circle(x, y, d)

    if (wink) {
        line(x - d/2, y, x + d/2, y);
    } else {
      fill (fc - 30);
      circle(x, y, d/2);
    }
}