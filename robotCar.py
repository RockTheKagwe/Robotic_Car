# Complete project details at https://RandomNerdTutorials.com/micropython-hc-sr04-ultrasonic-esp32-esp8266/
from hcsr04 import HCSR04
from dcmotor import DCMotor 
from time import sleep
from machine import Pin, PWM

sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)

frequency = 15000       
pin1 = Pin(16, Pin.OUT)    
pin2 = Pin(17, Pin.OUT)
pin3 = Pin(19, Pin.OUT)    
pin4 = Pin(21, Pin.OUT)

enable_left = PWM(Pin(13), frequency)
enable_right = PWM(Pin(12), frequency)
     
dc_motor_left = DCMotor(pin1, pin2, enable_left, 750, 1023)     
dc_motor_right = DCMotor(pin3, pin4, enable_right, 750, 1023)

while True:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    #sleep(1)
    dc_motor_left.forward(50)
    dc_motor_right.forward(50)  
    if (distance < 20):
        dc_motor_left.stop()
        dc_motor_right.stop()
        sleep(1)
        dc_motor_left.backwards(50)
        dc_motor_right.backwards(50)
    sleep(1)

    
