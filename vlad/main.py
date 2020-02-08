import nltk

import vlad.message_analyzer as bot

#nltk.download()
from naumow.dao import Dao

while True:
    message = input()
    dao = Dao()
    print(dao.get_answer(bot.get_response(message)))
