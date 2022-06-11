# Event: new message sent by user
# Handle: send bot response to server

from datetime import datetime

import account
from app import bot
import socketio

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

    reply = bot.get_response(data["content"])

    message = {
        'sender_id': account.user_id,
        'sender_name': f'{account.payload["first_name"]} {account.payload["last_name"]}',
        'sender': account.payload["username"],
        'content': reply,
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
