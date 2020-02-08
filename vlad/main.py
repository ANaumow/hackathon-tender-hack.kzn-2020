import nltk

import vlad.message_analyzer as bot

#nltk.download()



while True:
    message = input()
    print(bot.get_response(message))
