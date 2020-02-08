import nltk

import vlad.message_analyzer as bot

#nltk.download()
from naumow.dao import Dao

while True:
    message = input()
    dao = Dao()
    num = bot.get_response(message)
    #print(num)
    print(dao.execute("select `text` from hack.`key` where `answer_id` = " + str(num)))
    print(dao.get_answer(num)[0])
