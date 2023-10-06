from machine import Pin, PWM
import time

led = Pin("LED", Pin.OUT)
led.on()

pin_out = Pin(0, mode=Pin.OUT)
pwm_pin = PWM(pin_out)
pwm_freq = 50
pwm_pin.freq(pwm_freq)
print("PWM frequency is " + str(pwm_freq) + " Hz")

# beeping stops at 4% cca
# motor starts rotating at 5% cca
# motor stops speeding up at 6.8% cca
# motor stops rotating at 12% cca

cycle_ratio = 3
while True:
    DT = 65536*cycle_ratio/100
    pwm_pin.duty_u16(int(DT))
    print("Duty cycle is -> " + str(cycle_ratio) + " %")
    time.sleep(0.5)
    cycle_ratio += 0.1
    

'''while True:
    cycle_ratio = float(input("Set duty cycle -> "))/100
    
    
    if cycle_ratio < 0:
        pwm_pin.duty_u16(0)
        print("Duty cycle is set to 0%")
        print("Program ended.")
        break
    print("Duty cycle is set to " + str(cycle_ratio*100) + " %")
    
    DT = 65536*cycle_ratio
    pwm_pin.duty_u16(int(DT))'''
    