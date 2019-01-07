from server import sio, app

def expose_motor(motor):
  @sio.on('connect')
  def connect(sid, environ):
      print('connect ', sid)
      sio.emit("direction", motor.dir)
      sio.emit("speed", motor.speed)
      sio.emit("enable", motor.enable)

  @sio.on('disconnect')
  def disconnect(sid):
      print('disconnect ', sid)

  @sio.on("direction")
  def direction(sid, dir):
      print("direction ", dir)
      motor.set_dir(dir)

  @sio.on("enable")
  def enable(sid, en):
      print("enable ", en)
      motor.set_enable(en)

  @sio.on("speed")
  def enable(sid, speed):
      print("speed ", speed)
      motor.set_speed(speed)
