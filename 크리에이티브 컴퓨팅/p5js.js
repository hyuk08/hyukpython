let unit = 50;
let cols, rows;

function setup() {
  createCanvas(400, 400);
  background(0);
  cols = width/unit;
  rows = height/unit;
}

function draw() {
  background(220);
  randomSeed();
  
  for (let i=0; i<cols; i++) {
    for (let j=0; j<rows; j++) {
    
      let cx = i*unit + unit/2;
      let cy = j*unit + unit/2;

      let p = random();
      if (p > 0.9) {
        drawTarget(cx, cy, unit, random(2, mouseY/5));
      } else if (p > 0.1) {
        eye(cx, cy, unit, random(255), 3, keyIsPressed)
      } else if (mouseIsPressed) {
        fill(243, 138, 255)
        //아직 안 채웠음 ㅋㅋ
          } else {
          fill(0, 35, 232);
          stroke(243, 138, 255)
          circle(cx, cy, unit)
          }
        
      // circle(cx, cy, unit);
      // drawTarget(cx, cy, unit, random(2, mouseY/5));
      // let wink = random([true, false]);
      // eye(cx, cy, unit, random(255), 3, wink);

    }
  }

}

function eye(x, y, d, fc/*fillcolor*/, thickness, wink) {
  stroke(fc - 70);
  strokeWeight(thickness);
  // fill(fc);
  circle(x, y, d)

  if (wink) {
      line(x - d/2, y, x + d/2, y);
  } else {
    // fill (fc - 30);
    circle(x, y, d/2);
  }
}

function drawTarget(xloc, yloc, size, num) {
  const grayvalues = 255 / num;
  const steps = size / num;
  for (let i = 0; i < num; i++) {
    // fill(i * grayvalues);
    ellipse(xloc, yloc, size - i * steps, size - i * steps);
  }
}