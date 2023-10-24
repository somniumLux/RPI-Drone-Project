from machine import Pin, PWM
import time

led = Pin("LED", Pin.OUT)
led.on()

pin_out_1 = Pin(0, mode=Pin.OUT)
pwm_pin_1 = PWM(pin_out_1)
pin_out_2 = Pin(1, mode=Pin.OUT)
pwm_pin_2 = PWM(pin_out_2)
pin_out_3 = Pin(2, mode=Pin.OUT)
pwm_pin_3 = PWM(pin_out_3)
pin_out_4 = Pin(3, mode=Pin.OUT)
pwm_pin_4 = PWM(pin_out_4)

pwm_freq = 50
pwm_pin_1.freq(pwm_freq)
pwm_pin_1.freq(pwm_freq)
pwm_pin_2.freq(pwm_freq)
pwm_pin_4.freq(pwm_freq)

print("PWM frequency is " + str(pwm_freq) + " Hz")

def set_motor_pwm(pwm_pin_1, pwm_pin_2, pwm_pin_3, pwm_pin_4, duty_cycle):
    pwm_pin_1.duty_u16(duty_cycle)
    pwm_pin_2.duty_u16(duty_cycle)
    pwm_pin_3.duty_u16(duty_cycle)
    pwm_pin_4.duty_u16(duty_cycle)

# beeping stops at 4% cca
# motor starts rotating at 5% cca
# motor stops speeding up at 6.8% cca
# motor stops rotating at 12% cca

cycle_ratio = 3
DT = 65536*cycle_ratio/100

print("Initializing motors")
while True:
    DT = 65536*cycle_ratio/100
    set_motor_pwm(pwm_pin_1, pwm_pin_2, pwm_pin_3, pwm_pin_4, int(DT))

    time.sleep(0.2)
    cycle_ratio += 0.1
    if cycle_ratio >= 4.6:
        pwm_pin_1.duty_u16(0)
        pwm_pin_2.duty_u16(0)
        pwm_pin_3.duty_u16(0)
        pwm_pin_4.duty_u16(0)
        break
    
print("Motors are initialized")
while True:
    cycle_ratio = float(input("Input PWM value --> "))
    print(f"PWM is set to {}", cycle_ratio)
    if cycle_ratio < 0:
        break
    if cycle_ratio > 12:
        cycle_ratio = 12
        
    DT = 65536*cycle_ratio/100
    set_motor_pwm(pwm_pin_1, pwm_pin_2, pwm_pin_3, pwm_pin_4, int(DT))
    
    
    
    
    