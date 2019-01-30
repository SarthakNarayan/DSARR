#include <Servo.h>

int servo = 0;
int led0 = 0;
int led1 = 0;
int led2 = 0;
int led3 = 0;
int analog_left_back = 0;
int analog_right_back = 0;

Servo myservoleft;
Servo myservoright;

void setup() {
  Serial.begin(9600);
  pinMode(5, OUTPUT);
  myservoleft.attach(5);
  pinMode(3, OUTPUT);
  myservoright.attach(3);

}

void ser()
{
  while(!Serial.available());
  led0=Serial.readStringUntil('\t').toInt();
  led1=Serial.readStringUntil('\t').toInt();
  led2=Serial.readStringUntil('\t').toInt();
  led3=Serial.readStringUntil('\t').toInt();
  analog_left_back=Serial.readStringUntil('\t').toInt();
  analog_right_back=Serial.readStringUntil('\n').toInt();
}


void loop() {
  ser();
  /*
  if(led0 == 1)
  myservo.write(72);
  
  if(led1 == 1)
  myservo.write(90);
  
  
  if(led2 == 1)
  myservo.write(90);
  if(led3 == 1)
  myservo.write(180);
  */


    myservoleft.write(analog_left_back);
    myservoright.write(analog_right_back);
  
}
