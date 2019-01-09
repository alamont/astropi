import sys, os
import time
from motor import Motor
from server import sio, app
from sockets import expose_motor
import serial

SERIAL_PORT = os.getenv('SERIAL_PORT', "/dev/ttyUSB0")
SERIAL_PORT=None

STEP_PIN = 2
DIR_PIN = 3
EN_PIN = 4

motor = Motor(step_pin=STEP_PIN, 
              dir_pin=DIR_PIN, 
              en_pin=EN_PIN, 
              serial_port=SERIAL_PORT)
expose_motor(motor)
print(motor.get_all_registers())
  
input("press ENTER to terminate.")

motor.close(True)