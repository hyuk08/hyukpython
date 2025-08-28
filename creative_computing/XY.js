function setup() {
    createCanvas(500, 500);
    noStroke();
  }
  function draw() {
    let x = mouseX;
    let y = mouseY;
    let ix = width - mouseX;  // Inverse X
    let iy = height - mouseY; // Inverse Y
    background(126);
    fill(255, 150);
    ellipse(x, height/2, y, y);
    fill(0, 159);
    ellipse(ix, height/2, iy, iy);
  }