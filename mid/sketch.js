let song;
let value = 1;

/*
      화면을 마우스로 클릭하여 노래를 재생하고, 키패드로 인터랙션.
*/

function preload() {
  soundFormats('mp3');
  song = loadSound('deer.mp3');
}

function setup() {
  cnv = createCanvas(700, 700);
  cnv.mousePressed(canvasPressed);
  // cnv.mouseClicked(togglePlay);
  // background(220);
  // text('탭해서 재생하세요', 10, 20);
  fft = new p5.FFT();
}

function draw() {
  // frameRate(12);
  background(0);
  fill(195, 226, 221);
  text('한 번 탭하여 재생하세요', 10, 20);
  // let spectrum = fft.analyze();
  noStroke();
  SPD(value);
}

function canvasPressed() {
  song.play();
}

function SPD(input) {
  let spectrum = fft.analyze();

  for (let i = 0; i < spectrum.length; i++) {
    let x = map(i, 0, spectrum.length, 0, width * input);
    let h = -height + map(spectrum[i], 0, 255, height, 0);
    // rect(x, height, width / spectrum.length, h )
    for (let j = 0; j < 5; j++) {
      fill(random(215), random(226), random(221, 241));
      rect(x, height, width / spectrum.length, h);
    }
  }
}

function keyPressed() {
  if (key === '1') {
    value = 1;
  } else if (key === '2') {
    value = 3;
  } else if (key === '3') {
    value = 5;
  } else if (key === '4') {
    value = 7;
  } else if (key === '5') {
    value = 9;
  } else if (key === '6') {
    value = 11;
  } else if (key === '7') {
    value = 13;
  } else if (key === '8') {
    value = 17;
  } else if (key === '9') {
    value = 25;
  } else if (key === '0') {
    value = 40;
  }
}