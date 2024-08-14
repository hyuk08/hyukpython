function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);

  drawFace();
  drawMouth();
  draweyes();
}

function drawFace() {
  fill("yellow");
  ellipse(200, 200, 250, 250);
}

function drawMouth() {
  fill("pink");
  rect(180, 230, 40, 50);
}

function draweyes() {
  fill("black")
  arc(150, 170, 50, 50, 0, PI + HALF_PI);
  arc(250, 170, 50, 50, 0, PI + HALF_PI);
}