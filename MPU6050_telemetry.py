import machine
import time
import MPU6050

i2c = machine.I2C(1, sda=machine.Pin(14), scl=machine.Pin(15))
 
mpu = MPU6050.MPU6050(i2c)
mpu.wake()
mpu.write_lpf_range(5) # Low pass filter

while True:
    gyro = mpu.read_gyro_data()
    accel = mpu.read_accel_data()
    print("Gyro: " + str(gyro) + ", Accel: " + str(accel))
    time.sleep(0.05)