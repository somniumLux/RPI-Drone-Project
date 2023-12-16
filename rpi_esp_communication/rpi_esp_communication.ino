// UART Communication from ESP8266 to Raspberry Pi Pico
void setup() {
  Serial.begin(9600);  // Set the baud rate to match the Raspberry Pi Pico
}

void loop() {
    char receivedChar = Serial.write("Hello from ESP!\n");
    delay(1000);
}
