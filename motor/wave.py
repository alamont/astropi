import pigpio

pi = pigpio.pi() 

class Waves():
  def __init__(self, secs=1, pw=100):
    # self.wf = []
    self.secs = secs
    self.pw = pw
    self.wid = None
    self.wid_old = None
    self.waves = {}

    pi.wave_clear()

  def add_wave(self, gpio, hz):
    # self.wf = []
    self.waves[gpio] = hz
    for key, value in self.waves.items():
      self._add_wave(key, value)
    self.wid_old = self.wid
    self.wid = pi.wave_create()
    if self.wid_old is not None:
      pi.wave_delete(self.wid_old)

  def _add_wave(self, gpio, hz):  
    micros_left = int(self.secs * 1000000)
    transitions = int(hz * self.secs)
    micros = micros_left // transitions

    wf = []

    for t in range(transitions, 0, -1):
      micros = micros_left // t
      if (t & 1):# == (on & 1):
        wf.append(pigpio.pulse(0, 1<<gpio, micros))
        wf.append(pigpio.pulse(1<<gpio, 0, micros + self.pw))
      micros_left -= micros

    print("#pulses: ", pi.wave_add_generic(wf))
    # self.waves[gpio] = hz

  def clear_waves(self):
    pi.wave_clear()

  def send_waves(self):
    pi.wave_send_repeat(self.wid)
