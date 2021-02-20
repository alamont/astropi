import sys, os
import time
from motor import Motor
from altitude import Altitude
from altitude import Altitude
from server import sio, app
from sockets import expose_motors, expose_altitude  
import serial
import pigpio
from wave import Waves


SERIAL_PORT0 = os.getenv('SERIAL_PORT0', "/dev/ttyUSB0")
SERIAL_PORT1 = os.getenv('SERIAL_PORT1', "/dev/ttyUSB1")
SERIAL_PORT2 = os.getenv('SERIAL_PORT2', "/dev/ttyUSB2")
#SERIAL_PORT0=None
#SERIAL_PORT1=None

STEP_PIN = 2
DIR_PIN = 3
EN_PIN = 4

pigpio.pi().wave_clear()

waves = Waves(0.01)

motor0 = Motor(step_pin=3, 
              dir_pin=4, 
              en_pin=2, 
              serial_port=SERIAL_PORT0,
              motor_id=0,
              waves=waves)

motor1 = Motor(step_pin=27, 
              dir_pin=22, 
              en_pin=17,
              motor_id=1,
              serial_port=SERIAL_PORT1,
              waves=waves)

motor2 = Motor(step_pin=9, 
               dir_pin=11, 
               en_pin=10,
               motor_id=1,
               serial_port=SERIAL_PORT2,
               waves=waves)

print(motor0.ser)
print(motor1.ser)
print(motor2.ser)

print(motor0.get_all_registers())
print(motor1.get_all_registers())
print(motor2.get_all_registers())

altitude = Altitude(motor0, motor1)
#azimuth = Azimuth(motor2)

# expose_motors({0: motor0, 1: motor1})
expose_altitude(altitude)
#expose_azimuth(azimuth)

# expose_motor(motor1)
# print(motor.get_all_registers())
  
input("press ENTER to terminate.")

motor0.close(True)
motor1.close(True)
motor2.close(True)
