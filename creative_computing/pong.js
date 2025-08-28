let bx, by;
let vx, vy;
let bw;
let barX, barY;

let imageFile = "1.jpeg";

let imageLoaded = false;
let loadedImage;
let imageOpacity = 255;

let audio = new Audio('vine_boom.mp3');
audio.volume = 0.1;
let audio1 = new Audio('999.mp3');
audio1.volume = 0.05;

function preload() {

  loadedImage = loadImage(imageFile, img => {
    imageLoaded = true;
  });
}

function setup() {
  createCanvas(400, 300);

  bx = width / 2;
  by = height / 2;
  bw = 10;
  vx = 10;
  vy = random(0, 5);
  barX = 360;
  barY = 120;
}

function draw() {
  background(0);
  rect(bx, by, bw, bw);
  bx += vx;
  by += vy;

  if (bx < 0 || width < bx + bw) {
    vx *= -1;
  } else if (by < 0 || height < by + bw) {
    vy *= -1;
  }

  rect(barX, barY, bw / 2, bw * 4);
  if (keyIsDown(DOWN_ARROW)) {
    barY += 6;
  }

  if (keyIsDown(UP_ARROW)) {
    barY -= 6;
  }

  if (bx + bw > barX) {
    if (by + bw > barY && by < barY + bw * 4) {
      vx *= -1;
      fill(random(0, 255), random(0, 255), random(0, 255));
      audio.play();
      setTimeout(function () {
        audio.pause();
        audio.currentTime = 0;
      }, 1500);

      if (imageLoaded) {
        imageMode(CENTER);
        image(loadedImage, width / 2, height / 2);
        imageOpacity -= 2;
        tint(255, imageOpacity);
      }
    }
  }
  if (barY < 0 || barY + bw * 4 > height) {
    audio1.play();
    setTimeout(function () {
      audio1.pause();
      audio1.currentTime = 0;
    }, 1500);
  }
}