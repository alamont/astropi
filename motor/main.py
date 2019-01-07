import sys
import time
from motor import Motor
from server import sio, app
from sockets import expose_motor

STEP_PIN = 2
DIR_PIN = 3
EN_PIN = 4

motor = Motor(step_pin=STEP_PIN, dir_pin=DIR_PIN, en_pin=EN_PIN)
expose_motor(motor)
  
input("press ENTER to terminate.")

motor.close(True)