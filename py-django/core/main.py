import nltk
#nltk.download()


import core.message_analyzer as bot

# nltk.download()
from db.dao import Dao


def get_user_response(msg):
    message = str(msg)
    dao = Dao()
    num = bot.get_response(message)
    print(dao.get_answer(num)[0])
    return dao.get_answer(num)[0]