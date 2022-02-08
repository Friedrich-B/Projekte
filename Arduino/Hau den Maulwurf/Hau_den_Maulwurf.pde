import processing.serial.*;


Serial connection;
String input;


Unit[] units;
void setup(){
  size(1230, 1030);
  background(-9271232);
  stroke(0);
  fill(200);
  textSize(30);
  textAlign(CENTER);
  
  String portName = Serial.list()[0];
  connection = new Serial(this, portName, 9600);
  connection.bufferUntil('\n');
  
  units = new Unit[9];
  for (int y = 0, i = 0; y<3; y++){
    for (int x = 0; x<3; x++, i++){
        int xPos = 50+x*315;
        int yPos = 50+y*315; 
        units[i] = new Unit(xPos, yPos);
    }
  }
  
  render();
}


int lastPressed;
int timePressed;
String score = "0";
int score1;
void draw(){
  if (input != null){
    String action = input.substring(0, 1);
    if (action.equals("S")){
      input = input.replace("\n","");
      score = input.substring(1);
    } else {
      int unitIndex = int(input.substring(1, 2)) - 1;
      units[unitIndex].setState(action);
      if (action.equals("P")){
         lastPressed = unitIndex;
         timePressed = millis();
      }
      input = null;
     render();
    }
  }
        if (millis() >= (timePressed+100)){
         units[lastPressed].setState("D");
         timePressed += 1000000;
         lastPressed = -1;
         render();
      }
}

void render(){
     background(-9271232);
     for (int i = 0; i < 9; i++){
       units[i].update();
     }
     text("Score:", 1100, 500);
     text(score, 1100, 530);
     if (score.equals("0")){
       text("Drücke \"*\",\n um das Spiel\n zu starten.", 1100, 600);
     }
}

void serialEvent(Serial connection) {
  input = connection.readString();
}

class Unit{
  int x, y;
  color state;
  
  Unit(int x, int y){
     this.x = x;
     this.y = y;
     this.state = State.DEFAULT;
  }
  
  void update() {
    fill(state);
    rect(x, y, 300, 300);
    fill(200);
    
  }
  
  void setState(String newState){
    switch(newState){
      case "A":
        state = State.MOLE;
        break;
      case "P":
        state = State.PRESSED;
        break;
      case "D":
        state = State.DEFAULT;
        break;
    }
  }
}

class State{
  public static final color PRESSED = -346522;
  public static final color MOLE = -8766946;
  public static final color DEFAULT = -6572960;
}
