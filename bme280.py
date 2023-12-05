from machine import Pin, I2C
from time import sleep
import math
import bme280

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
last_altitude = 0.

def calculate_altitude(pressure, temperature):
    pressure_at_sea_level = float(1013.25)
    temperature_at_sea_level = float(288.15)
    earth_molar_mass = float(0.029)
    gravity = float(9.81)
    gas_constant = float(8.314)
    lapse_rate = float(-0.0065)
    
    exponent = (gas_constant*lapse_rate)/(gravity*earth_molar_mass)
    altitude = temperature_at_sea_level/lapse_rate*(1-(pressure/pressure_at_sea_level)**exponent)
    return altitude

def ewma_filter(current_value, last_value):
    filtered_value = last_value + 0.4*(current_value - last_value);
    last_value = filtered_value;
    return filtered_value, last_value

while True:
    bme = bme280.BME280(i2c=i2c)
    temperature_str, pressure_str, humidity_str = bme.values
    
    temperature = float(temperature_str[:-1])
    pressure = float(pressure_str[:-3])
    humidity = float(humidity_str[:-1])
      
    altitude = calculate_altitude(pressure, temperature)
    filtered_altitude, last_altitude = ewma_filter(altitude, last_altitude)
    print(filtered_altitude)
    
    sleep(0.005)
