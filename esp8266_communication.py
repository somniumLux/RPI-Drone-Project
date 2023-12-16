# UART Communication from Raspberry Pi Pico to ESP8266
import machine
import utime
import ujson as json

tx_pin = machine.Pin(0)
rx_pin = machine.Pin(1)
uart = machine.UART(0, 9600, 8, None, tx=tx_pin, rx=rx_pin)

while True:
    if uart.any():
        json_data = uart.readline()
        
        try:
            data = json.load(json_data)
            
            aceel_x = data["x"]
            aceel_y = data["y"]
            aceel_z = data["z"]
            
            print(print(f"x: {x}, y: {y}, z: {z}"))
            
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

"""while True:
    if uart.any():
        received_data = uart.readline()
        print(received_data)
    
    utime.sleep(1)"""
