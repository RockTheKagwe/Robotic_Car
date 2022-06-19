#This is the library that is used to control the DC Motor.
class DCMotor:      
  def __init__(self, pin1, pin2, enable_pin, min_duty=750, max_duty=1023):
        self.pin1=pin1
        self.pin2=pin2
        self.enable_pin=enable_pin
        self.min_duty = min_duty
        self.max_duty = max_duty

  #This is the function used to drive the motor forward.
  def forward(self,speed):
    self.speed = speed
    self.enable_pin.duty(self.duty_cycle(self.speed))
    self.pin1.value(0)
    self.pin2.value(1)

  #This is the function used to drove the motor backwards. 
  def backwards(self, speed):
        self.speed = speed
        self.enable_pin.duty(self.duty_cycle(self.speed))
        self.pin1.value(1)
        self.pin2.value(0)

  #This is the function that is used to sop the motor from moving in any direction.
  def stop(self):
    self.enable_pin.duty(0)
    self.pin1.value(0)
    self.pin2.value(0)

  #This is the function used for Pulse Width Modulation, which is used in speed control of the motor. 
  def duty_cycle(self, speed):
   if self.speed <= 0 or self.speed > 100:
        duty_cycle = 0
   else:
    duty_cycle = int(self.min_duty + (self.max_duty - self.min_duty)*((self.speed-1)/(100-1)))
    return duty_cycle