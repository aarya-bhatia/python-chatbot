from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask

bot = ChatBot(
    'Buddy',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.MathematicalEvaluation']
)

corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train('chatterbot.corpus.english')

app = Flask(__name__)


@app.route('/response/<message>', methods=['GET'])
def GET_response(message):
    if not message:
        return "", 400

    response = bot.get_response(message)
    print("BOT:", response)
    return response.text, 200


def main():
    name = input("Enter Your Name: ")
    print("Welcome to the Bot Service,", name, "!")
    print("Type 'Bye' to exit.")
    while True:
        request = input(name + ':')
        if request == 'Bye' or request == 'bye':
            print('Bot: Bye')
            break
        else:
            response = bot.get_response(request)
            print('Bot:', response)


if __name__ == '__main__':
    main()
