class AxisControl():
  def __init__(self, axis, accel=100, max_speed=5000):
    self.axis = axis
    self.accel = accel
    self.max_speed = max_speed
    self.speed = 0
  
  def 