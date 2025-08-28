let angles = [30, 10, 45, 35, 60, 38, 75, 67];

function setup() {
  createCanvas(400, 400);
  noStroke();
  noLoop(); // 프로그램 시작시 한 번 실행 뒤 멈추기
}

function draw() {
  background(100);
  pieChart(20, 20, 300, angles);
}

function pieChart(x, y, diameter, data) {
  let lastAngle = 0;
  for (let i = 0; i < data.length; i++) {
    let gray = map(i, 0, data.length, 0, 255);
    fill(gray);
    arc(
      x,
      y,
      diameter,
      diameter,
      lastAngle,
      lastAngle + radians(angles[i])
    );
    lastAngle += radians(angles[i]);
  }
}