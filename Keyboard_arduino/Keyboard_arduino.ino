#include <Keyboard.h>

char i, intKeyPressed=0, charFlash=0 ;
int intAnalogValue=0;
char const charDigitalKeyMap[] = {'1','2','3','4','5','6','7','8','9'};
char const charAnalogKeyMap[] = {'A','B','C','D','E','F','G','H','I','J','K'};
char const analogInputPin = 0;
int const intADCRanges[][2] = {{0,38},{38,119},{119,205},{205,290},{290,375},{375,462},{462,550},{550,645},{645,737},{737,817},{817,898},{898,1024}};
#define DIGITAL_INPUTS 9
#define ANALOG_KEYS 11




void setup() {
  
  //
  // Initialization of Keyboard function, 
  // to allow to send chacters to PC over USB like PC keyboard.
  //
  Keyboard.begin();

  // initatilization of the IO pins
  pinMode(0,INPUT_PULLUP);
  pinMode(1,INPUT_PULLUP);
  pinMode(2,INPUT_PULLUP);
  pinMode(3,INPUT_PULLUP);
  pinMode(4,INPUT_PULLUP);
  pinMode(5,INPUT_PULLUP);
  pinMode(6,INPUT_PULLUP);
  pinMode(7,INPUT_PULLUP);
  pinMode(8,INPUT_PULLUP);
  
  
  pinMode(13,OUTPUT); // Green Led
}

void loop() {
  // put your main code here, to run repeatedly:
  // String stringMessage = "";
  delay(200);
  intKeyPressed = 0;
  
  //
  // scaning digital inputs
  //  
  for (i=0; i<DIGITAL_INPUTS; i++)
    if (!digitalRead(i)){
      intKeyPressed = charDigitalKeyMap[i];
      break;
    }

  //
  // scaning analog input
  //
  intAnalogValue = analogRead(analogInputPin);
  for (i=0; i<ANALOG_KEYS; i++)
    if (intAnalogValue >= intADCRanges[i][0] && intAnalogValue < intADCRanges[i][1]){
      intKeyPressed = charAnalogKeyMap[i];
      break;
    }
       
  //stringMessage = String(intAnalogValue,DEC);
  //Keyboard.println(stringMessage);
   
  //
  // if any key was pressed send code to PC
  //
  if (intKeyPressed)
    Keyboard.write(intKeyPressed);
  
  // 
  //  flash the led
  //
  digitalWrite(13,charFlash); 
  charFlash = ~charFlash;
}
