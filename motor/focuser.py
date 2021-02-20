import pigpio
import time

pi = pigpio.pi()

class Focuser():
    def __init__(self, pin):
        self.pin = pin
        pi.set_servo_pulsewidth(self.pin, 0)

    def step_right(self, dir):
        pi.set_servo_pulsewidth(self.pin, 1600)
        time.sleep(0.1)
        pi.set_servo_pulsewidth(self.pin, 1500)        
    def step_left(self, dir):
        pi.set_servo_pulsewidth(self.pin, 1600)
        time.sleep(0.1)
        pi.set_servo_pulsewidth(self.pin, 1500)

    def close(self):
        print("close")
        pi.set_servo_pulsewidth(self.pin, 0)