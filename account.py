import requests

user_id = "62a3841f352f6000187d14e2"

# base_url = "http://aaryab2-messenger-app.herokuapp.com"
base_url = "http://localhost:3000"

payload = {
    "first_name": "Chat",
    "last_name": "Bot",
    "username": "bot123",
    "email": "bot@example.com",
    "password": "Test@123",
}

headers = {}
headers["Content-Type"] = "application/x-www-form-urlencoded"

def signup():
    data = '&'.join([f'{key}={payload[key]}' for key in payload])
    response = requests.post(base_url+'/sign-up', data=payload, headers=headers)
    print(response.text)

def login():
    data = f'username={payload["username"]}&password={payload["password"]}'
    response = requests.post(base_url+'/sign-in',headers=headers,data=data)

    if response.status_code // 100 == 2:
        print('OK')
    else:
        print(response.status_code)
        exit(1)
