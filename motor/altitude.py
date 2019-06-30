import pigpio
import uart
import serial
import threading
import functools
from motor import Motor

def inv(b):
  return not bool(b)

class Altitude():
  def __init__(self, motor_l, motor_r, speed=1000, dir=1, enable=0):
    self.motor_l = motor_l
    self.motor_r = motor_r
    
    self.speed = speed
    self.dir = dir
    self.enable = enable

    self.set_speed(self.speed)
    self.set_dir(self.dir)
    self.set_enable(self.enable)

  def set_speed(self, speed):
    self.motor_l.set_speed(speed)
    self.motor_r.set_speed(speed)

  def set_dir(self, dir):
    self.motor_l.set_dir(dir)
    self.motor_r.set_dir(inv(dir))

  def set_enable(self, en):
    self.motor_l.set_enable(en)
    self.motor_r.set_enable(en)

  def close(self, stop=False):
    self.motor_l.close(stop)
    self.motor_l.close(stop)