let unit = 10;
let cols, rows;

function setup() {
    createCanvas(400, 400);
    background(0);
    cols = width / unit;
    rows = height / unit;
}

function draw() {
    background(220);

    for (let i = 0; i < cols; i++) {
        for (let j = 0; j < rows; j++) {

            let cx = i * unit + unit / 2;
            let cy = j * unit + unit / 2;

            let d = dist(cx, cy, mouseX, mouseY);
            if (d < unit / 0.1) {
                fill("white");
            } else {
                fill("black");
            }

            if (mouseIsPressed) {
                textSize(100);
                text("Hello", mouseX / 2.3, mouseY);
                fill(0);
            }
            circle(cx, cy / 2, unit);

        }
    }
}