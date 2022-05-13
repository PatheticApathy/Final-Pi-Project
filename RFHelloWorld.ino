/*
* Arduino Wireless Communication Tutorial
*     Example 1 - Transmitter Code
*                
* by Dejan Nedelkovski, www.HowToMechatronics.com
* 
* Library: TMRh20/RF24, https://github.com/tmrh20/RF24/
*/

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(9, 8); // CE, CSN

const byte address[6] = "DuckB";

void setup()
{
  Serial.begin(9600);
  pinMode(3,INPUT);
  pinMode(4,INPUT);
  pinMode(5,INPUT);
  pinMode(6,INPUT);
  pinMode(7,INPUT);

  radio.begin();
  radio.openWritingPipe(address);
  //radio.setPALevel(RF24_PA_MIN);
  radio.setChannel(50);
  radio.stopListening();
}

void loop()
{
  int resetLight = digitalRead(3);
  int moveForward = digitalRead(4);
  int moveBack = digitalRead(5);
  int turnLeft = digitalRead(6);
  int turnRight = digitalRead(7);
  if (moveForward == 1)
  {
    Serial.println("forward recieved");
    const char text[] = "Move Forward";
    radio.write(&text, sizeof(text));
  }
  else if (moveBack == 1)
  {
    Serial.println("back recieved");
    const char text[] = "Move Back";
    radio.write(&text, sizeof(text));
  }
  else if (turnLeft == 1)
  {
    Serial.println("left recieved");
    const char text[] = "Turn Left";
    radio.write(&text, sizeof(text));
  }
  else if (turnRight == 1)
  {
    Serial.println("right recieved");
    const char text[] = "Turn Right";
    radio.write(&text, sizeof(text));
  }
  else if (resetLight == 1)
  {
    Serial.println("Reset Light");
    const char text[] = "Reset Light";
    radio.write(&text, sizeof(text));
  }
  else
  {
    Serial.println("Nothing recieved");
    const char text[] = "Stop";
    radio.write(&text, sizeof(text));
  }
}
