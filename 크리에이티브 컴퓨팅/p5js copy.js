
function setup() {
  createCanvas(720, 400);
  background(51);
  noStroke();
  noLoop();
}

// function draw() {
//   drawTarget(width * 0.25, height * 0.4, 200, 4);
//   drawTarget(width * 0.5, height * 0.5, 300, 10);
//   drawTarget(width * 0.75, height * 0.3, 120, 6);
// }

function draw() {
  drawTarget(150, 150, 200, 10)
}

function drawTarget(xloc, yloc, size, num) {
  const grayvalues = 255 / num;
  const steps = size / num;
  for (let i = 0; i < num; i++) {
    fill(i * grayvalues);
    ellipse(xloc, yloc, size - i * steps, size - i * steps);
  }
}
