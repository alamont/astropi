import pigpio
import uart
import serial
import threading
import functools

class Motor():
  def __init__(self, step_pin, dir_pin, en_pin, motor_id, waves, speed=1000, dir=1, enable=1, serial_port=None):
    self.step_pin = step_pin
    self.dir_pin = dir_pin
    self.en_pin = en_pin
    self.ser = None
    self.wave_id = None
    self.waves = waves
    self.motor_id = motor_id
    if serial_port:
      baudrate = 115200
      self.ser = serial.Serial(serial_port, baudrate, timeout=0)
    
    self.pi = pigpio.pi()
    if not self.pi.connected:
      exit()
    else:
      print("pigpio connected")

    self.pi.set_mode(step_pin, pigpio.OUTPUT)
    self.pi.set_mode(dir_pin, pigpio.OUTPUT)
    self.pi.set_mode(en_pin, pigpio.OUTPUT)

    self.speed = speed
    self.dir = dir
    self.enable = enable

    self.pi.write(self.en_pin, self.enable) # Enable Driver
    self.pi.write(self.dir_pin, self.dir)

    self.set_speed(self.speed)

  def set_speed(self, speed):
    
    self.waves.add_wave(self.step_pin, speed)
    self.waves.send_waves()

    # self.waveforms[self.motor_id] = [
    #   pigpio.pulse(1<<self.step_pin, 0, speed//10),
    #   pigpio.pulse(0, 1<<self.step_pin, speed-speed//10)
    # ]

    # # waveform = self.waveforms.
    # waveform = functools.reduce(lambda x, value:x + value, self.waveforms.values(), [])

    # # waveform.append(pigpio.pulse(1<<2, 0, 100))
    # # waveform.append(pigpio.pulse(0, 1<<2, 900))
    # # if self.wave_id is not None:
    #   # self.pi.wave_delete(self.wave_id)
    # self.pi.wave_clear()

    # self.pi.wave_add_generic(waveform)
    # wave = self.pi.wave_create()
    # self.pi.wave_send_repeat(wave)

  def set_dir(self, dir):
    self.pi.write(self.dir_pin, dir)

  def set_enable(self, en):
    self.pi.write(self.en_pin, en)

  # def set_mstep_res(self, mstep_res):
  #   uart.write()

  def close(self, stop=False):
    print("close")
    if stop:
      self.pi.write(self.en_pin, 1)
    self.pi.wave_tx_stop() # stop waveform
    self.pi.wave_clear() # clear all waveforms
    self.pi.stop()

  def get_all_registers(self):
    if self.ser:
      return uart.read_all(self.ser)
    else:
      return {}