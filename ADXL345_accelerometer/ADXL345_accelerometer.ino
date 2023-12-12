#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_ADXL345_U.h>

Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified();

void setup() {

  // ESP2866 board pins are:
  // D1 - SCL
  // D2 - SDA

  Serial.begin(9600);

  if (!accel.begin()) {
    Serial.println("Sensor not found");
    while(1);
  }

}

void loop() {
      
  sensors_event_t event;
  accel.getEvent(&event);

  /*Serial.print(event.acceleration.x);
  Serial.print(" ");
  Serial.print(event.acceleration.y);
  Serial.print(" ");
  Serial.println(event.acceleration.z);*/

  Serial.print("X: "); Serial.print(event.acceleration.x); Serial.println("");
  Serial.print("Y: "); Serial.print(event.acceleration.y); Serial.println("");
  Serial.print("Z: "); Serial.print(event.acceleration.z); Serial.println("");
  Serial.println();  

  delay(50);

}