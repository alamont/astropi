from server import sio, app
import json

def expose_motors(motors):
    @sio.on('connect')
    def connect(sid, environ):
        print('connect ', sid)
        # print(motor.motor_id)
        for motor_id in motors:
            motor = motors[motor_id]
            sio.emit("motor", json.dumps({"motorId": motor.motor_id, 
                                        "dir": motor.dir,
                                        "speed": motor.speed,
                                        "enable": motor.enable}))
    #   sio.emit("speed", json.dumps({"motorId": motor.id, "speed": motor.speed)
    #   sio.emit("enable", json.dumps({"motorId": motor.id, "enable": motor.enable)

    @sio.on("motor")
    def motor_socket(sid, data):
        # data = json.loads(json_data)
        print(data)
        if data["motorId"] in motors:
            motor = motors[data["motorId"]]
            dir = data.get("dir", None)
            enable = data.get("enable", None)
            speed = data.get("speed", None)
            print(dir, enable, speed)
            if dir is not None: motor.set_dir(dir)
            if enable is not None: motor.set_enable(enable)
            if speed is not None: motor.set_speed(speed)

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