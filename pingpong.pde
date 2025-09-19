void setup() {
  fullScreen();
  background(0,0,0);
}

int ballY = (
100
);

int ballX = (
1000
);

int fartX = (0);
int fartY = (10);
int fartINC = (0);
int LIVES = (3);
int SCORE = (0);

int fill1 = 0;
int fill2 = 0;
int fill3 = 0;

boolean colorPhase1 = true;
boolean colorPhase2 = false;
boolean colorPhase3 = false;
boolean c = false;

void draw() { // loop
  if (colorPhase1) {
    if (c) {
      fill3 = fill3-1;
    }
    fill1 = fill1+1;
    if (fill1 == 255) {
      colorPhase2 = true;
      colorPhase1 = false;
    }
  }
  if (colorPhase2) {
    fill2 = fill2+1;
    fill1 = fill1-1;
    if (fill2 == 255) {
      colorPhase3 = true;
      colorPhase2 = false;
    }
  }
  if (colorPhase3) {
    fill2 = fill2-1;
    fill3 = fill3+1;
    if (fill3 == 255) {
        c= true;
        colorPhase1 = true;
        colorPhase3 = false;
      }
    }
  
  
  if (((ballX+30 < mouseX+150 & ballX+30 > mouseX-150) & ((ballY+30 > 787.5)&(ballY+30 < 812.5)))
  ||((ballX-30 < mouseX+150 & ballX-30 > mouseX-150) & ((ballY-30 > 787.5)&(ballY-30 < 812.5)))){
    fartINC = fartINC + 1;
    if (ballX > mouseX) {fartX = 5+fartINC;}
    if (ballX < mouseX) {fartX = -5-fartINC;}
    SCORE = SCORE + 1;
    fartY = -10 - fartINC;
  }
  if (ballX < 20) {fartX = 5+fartINC; fartINC = fartINC + 1;}
  if (ballX > width-30) {fartX = -5-fartINC; fartINC = fartINC + 1;}
  if (ballY < 50) {
    fartY = 10 + fartINC;
  };
  if ((ballY > height)&(LIVES > 0)) {
    ballY = 50;
    ballX = width/2;
    delay(3);
    LIVES = LIVES-1;
    fartX = 0;
  }
  ballY = ballY + fartY ; //endrer ballens høyde
  ballX = ballX + fartX;
  fill(255, 255, 255, 255); // setter fargen til hvit
  rect(0, 0, width, height); //setter en ny bakgrunn over de gamle
  fill(0); //setter fargen til svart
  fill(fill1,fill2,fill3);
  circle(ballX,ballY,60); //tegner ballen
  fill(0);
  rect(mouseX-150, 800, 300, 25); //tegner rektanglen ved musen
  fill(255,0,0);
  textSize(50);
  text(SCORE,width-100,100);
  }
  
  if (mousePressed) {
    mouseX = ballX;
  }
