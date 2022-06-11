from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot(
    'Buddy',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.MathematicalEvaluation']
)

corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train('chatterbot.corpus.english')


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
