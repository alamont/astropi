import pigpio

pi = pigpio.pi()
# pigpio.pi.set_servo_pulsewidth(17, 0)    # off
pi.set_servo_pulsewidth(14, 1000) # safe anti-clockwise
# pigpio.pi.set_servo_pulsewidth(17, 1500) # centre
# pigpio.pi.set_servo_pulsewidth(17, 2000) # safe clockwise