from bot import bot
from flask import Flask

app = Flask(__name__)


@app.route('/response/<message>', methods=['GET'])
def GET_response(message):
    global bot
    if not message:
        return "", 400

    response = bot.get_response(message)
    print("BOT:", response)
    return response.text, 200
