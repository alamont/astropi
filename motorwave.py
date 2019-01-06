import sys
import time
import random
import pigpio
import socketio
import eventlet
import threading

sio = socketio.Server()
app = socketio.WSGIApp(sio)

STEP_PIN = 2
DIR_PIN = 3
EN_PIN = 4

pi = pigpio.pi()

if not pi.connected:
   exit()

pi.set_mode(STEP_PIN, pigpio.OUTPUT)

state = {
  "enable": 0,
  "direction": 1,
  "speed": 1000
}

pi.write(EN_PIN, 0) # Enable Driver
pi.write(DIR_PIN, 1) # Set direction

def set_speed(speed):
  waveform = []

  waveform.append(pigpio.pulse(1<<STEP_PIN, 0, speed//10))
  waveform.append(pigpio.pulse(0, 1<<STEP_PIN, speed-speed//10))

  pi.wave_clear()

  pi.wave_add_generic(waveform)
  wave = pi.wave_create()
  pi.wave_send_repeat(wave)


set_speed(state["speed"])

@sio.on('connect')
def connect(sid, environ):
    print('connect ', sid)
    sio.emit("direction", state["direction"])
    sio.emit("speed", state["speed"])
    sio.emit("enable", state["enable"])

@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)

@sio.on("direction")
def direction(sid, data):
    print("direction ", data)
    state["direction"] = data
    pi.write(DIR_PIN, state["direction"])

@sio.on("enable")
def enable(sid, data):
    print("enable ", data)
    state["enable"] = data
    pi.write(EN_PIN, state["enable"])

@sio.on("speed")
def enable(sid, data):
    print("speed ", data)
    state["speed"] = data
    set_speed(state["speed"])
  

def serve_app(_sio, _app):
    app = socketio.Middleware(_sio, _app)
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)

wst = threading.Thread(target=serve_app, args=(sio,app))
wst.daemon = True
wst.start()




input("press ENTER to terminate.")

pi.wave_tx_stop() # stop waveform
pi.wave_clear() # clear all waveforms
pi.stop()
