# Event: new message sent by user
# Handle: send bot response to server

from datetime import datetime

import account
import socketio
import requests

base_url = account.base_url
sio = socketio.Client(engineio_logger=True, reconnection=True)


def register():
    data = {
        "socket_id": sio.sid,
        "user_id": account.user_id,
        "username": account.payload["username"]
    }
    sio.emit('register', data)


@sio.event
def connect():
    print('connection established')
    register()


@sio.event
def message(data):
    global sent

    if data["sender_id"] == account.user_id:
        print("Message sent: ", data["content"])
        return

    response = requests.get('http://localhost:5000/response/' + data["content"])
    content = response.text

    message = {
        'sender_id': account.user_id,
        'sender_name': f'{account.payload["first_name"]} {account.payload["last_name"]}',
        'sender': account.payload["username"],
        'content': content,
        'time': datetime.now().isoformat()
    }

    print('Message from: ', data["sender_name"])
    sio.emit('message', message)


@sio.event
def disconnect():
    print('disconnected from server')


sio.connect(base_url)
sio.wait()
print('SID:', sio.sid)
