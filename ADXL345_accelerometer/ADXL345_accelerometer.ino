#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_ADXL345_U.h>
#include <ArduinoJson.h>

Adafruit_ADXL345_Unified accelerometer = Adafruit_ADXL345_Unified();

void setup() {

  // ESP2866 board pins are:
  // D1 - SCL
  // D2 - SDA

  Serial.begin(9600);

  if (!accelerometer.begin()) {
    Serial.println("Sensor not found");
    while(1);
  }

}

void loop() {
      
  sensors_event_t event;
  accelerometer.getEvent(&event);

  Serial.print(event.acceleration.x);
  Serial.print(" ");
  Serial.print(event.acceleration.y);
  Serial.print(" ");
  Serial.println(event.acceleration.z);

  /*StaticJsonDocument<200> accelData;
  accelData["x"] = event.acceleration.x;
  accelData["y"] = event.acceleration.y;
  accelData["z"] = event.acceleration.z;

  String jsonData;
  serializeJson(accelData, jsonData);
  Serial.print(jsonData);*/

  delay(1000);

}