let bx, by; //ballX, ballY, ball_x, ball_y
let vx, vy;
let bw; // ballWidth

let barX, barY;



function setup() {
  createCanvas(400, 300);
  
  bx = width/2;
  by = height/2;
  bw = 20;
  
  vx = random(-5, 5);
  vy = 2;
  
  barX = 360;
  barY = 120;
  
}

function draw() {
  background(0);
  
  drawBall(bx, by, bw);
  moveBall();
  bounceBall();
  drawBar();
  handleKeyEvent();
}


function drawBall(x, y, w) {
    rect(x, y, w, w);
}


function moveBall() {
    bx = bx + vx;
    by = by + vy;
}


function bounceBall() {
    //bounceWall
    if (bx < 0 || width < bx+bw) {
        vx = vx * -1;
      }
      
      if (by < 0 || height < by+bw) {
        vy = vy * -1;
      }
    // bounceBar
    if (bx+bw > barX) {  
    if (by+bw > barY && by < barY+bw*4) {
        vx = vx * -1;
    //   fill(random(100, 255));
        }
    }
}


function drawBar() {
    rect(barX, barY, bw, bw*4);
}


function handleKeyEvent() {
    if (keyIsDown(DOWN_ARROW)) {
        barY = barY + 5;
      }
      
    if (keyIsDown(UP_ARROW)) {
        barY = barY - 5;
      }
}