import socketio
import eventlet
import threading

sio = socketio.Server()
app = socketio.WSGIApp(sio)

def serve_app(_sio, _app):
    app = socketio.Middleware(_sio, _app)
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)

wst = threading.Thread(target=serve_app, args=(sio,app))
wst.daemon = True
wst.start()