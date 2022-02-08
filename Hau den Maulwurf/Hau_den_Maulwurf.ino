// Robin, Friedrich
#include <Keypad.h>


unsigned long points;
unsigned long timer;
bool play;

// Einstellungen der Tastaur
const byte rows = 4;
const byte cols = 3;
char keys[rows][cols] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};

// Pins der Reihen
byte rowPins[rows] = {2,3,4,5};
// Pins der Spalten
byte colPins[cols] = {6,7,8};

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, rows, cols );


void setup() {
  points = 0;
  play = false;
  Serial.begin(9600);
}


void loop() {
  
  // Spiel + Timer start wenn "*" gedrückt
  if(!play){
    char start  = keypad.getKey();
    if(start != NO_KEY && String(start).equals("*")){
      play = true;
      timer = millis() + 60000;
    }
  }
  
  // Spiel
  if(play && millis() <= timer){
    
    // Maulwurf wird gesetzt
    int mole = random(1, 9);
    Serial.println("A" + String(mole));

    // Dauer bis der Maulwurf automatisch verschwindet
    unsigned long endTime = millis()+1500;

    // passiert solange Maulwurf vorhanden
    while(millis() < endTime){
      char key = keypad.getKey();

      // gedrückte Taste: Maulwurf tot?
      if(key != NO_KEY && String(key).equals(String(mole))){
          Serial.println("P" + String(key));
          points += 1;
          break;
        } else if(key != NO_KEY && !String(key).equals("*") && !String(key).equals("0") && !String(key).equals("#")){
        Serial.println("P" + String(key));
      }
    }

    // Maulwurf entfernen
    int outputDelay = 100;
    delay(outputDelay);
    Serial.println("D" + String(mole));
    delay(outputDelay);
    Serial.println("S" + String(points));
    delay(outputDelay);
  } else {
    play = false;
    points = 0;
  }
}

