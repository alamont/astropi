import pigpio

class Motor():
  def __init__(self, step_pin, dir_pin, en_pin, speed=1000, dir=1, enable=0):
    self.step_pin = step_pin
    self.dir_pin = dir_pin
    self.en_pin = en_pin
    
    self.pi = pigpio.pi()
    if not self.pi.connected:
      exit()

    self.speed = speed
    self.dir = dir
    self.enable = enable

    self.pi.write(self.en_pin, self.enable) # Enable Driver
    self.pi.write(self.dir_pin, self.dir)

    self.set_speed(self.speed)

  def set_speed(self, speed):
    waveform = []

    waveform.append(pigpio.pulse(1<<self.step_pin, 0, speed//10))
    waveform.append(pigpio.pulse(0, 1<<self.step_pin, speed-speed//10))

    self.pi.wave_clear()

    self.pi.wave_add_generic(waveform)
    wave = self.pi.wave_create()
    self.pi.wave_send_repeat(wave)

  def set_dir(self, dir):
    self.pi.write(self.dir_pin, dir)

  def set_enable(self, en):
    self.pi.write(self.en_pin, en)

  def close(self, stop=False):
    if stop:
      self.pi.write(self.en_pin, 1)
    self.pi.wave_tx_stop() # stop waveform
    self.pi.wave_clear() # clear all waveforms
    self.pi.stop()