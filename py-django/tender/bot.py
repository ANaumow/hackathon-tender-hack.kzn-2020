import io

import random

import string  # to process standard python strings

import warnings

import nltk
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

import warnings

warnings.filterwarnings('ignore')

from nltk.stem import WordNetLemmatizer

nltk.download('popular', quiet=True)  # for downloading packages

nltk.download('punkt')  # first-time use only

nltk.download('wordnet')  # first-time use only

with open('D:\python\django\\tender_hack\\tender\chatbot.txt', 'r', encoding='utf8', errors='ignore') as fin:
    raw = fin.read().lower()

sent_tokens = nltk.sent_tokenize(raw)  # converts to list of sentences

word_tokens = nltk.word_tokenize(raw)  # converts to list of words

lemmer = WordNetLemmatizer()


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


BAD_WORDS = ['сучара', 'хуйня', 'блят', 'бляд', 'пидарас', 'ипись', 'изъеб', 'еблан', 'ебеный', 'ебущий', 'ебанашка',
             'ебырь', 'хуище', 'гребан', 'уебище', 'уебан', 'феееб', '6ляд', 'сцука', 'ебали', 'пестато', 'ебало',
             'ебли', 'ебло', 'ебанут', 'ебут', 'заебу', 'выебу', 'хуйло', 'нехе', 'неху', 'ниху', 'нихе', 'ибанут',
             'fuck', 'хули', 'хуля', 'хуе', 'хуё', 'мудл', 'хер', 'пидар', 'наху', 'педер', 'пидер', 'пидир', 'ёбну',
             'ебну', 'ебыр', 'заеб', 'заёб', 'ебен', 'блятc', 'ебли', 'аебли', 'ебло', 'заебло', 'переебло', 'отебло',
             'отъебло', 'отьебло', 'ебеш', 'выеб', 'отъеб', 'отьеб', 'перееб', 'хуйла', 'заеб', 'хую', 'иннах', '6ля',
             '6ля', 'блЯ', 'бля', 'бля', 'хуило', 'хуюше', 'сука', 'ъеб', 'ъёб', 'бляд', 'блябу', 'бля бу', 'залупа',
             'хера', 'пизжен', 'ёпта', 'епта', 'пистапол', 'пизда', 'залупить', 'ебать', 'мудо', 'манда', 'мандавошка',
             'мокрощелка', 'муда', 'муде', 'муди', 'мудн', 'мудо', 'пизд', 'хуе', 'похую', 'похуй', 'охуи', 'ебля',
             'пидорас', 'пидор', 'херн', 'щлюха', 'хуй', 'нах', 'писдеш', 'писдит', 'писдиш', 'нехуй', 'ниибаца',
             'отсоси', 'долбаеб', 'ебу']

GREETING_INPUTS = ("привет", "здравствуйте", "хей", "добрый день", "доброе утро", "добрый вечер", 'хай',)

GREETING_RESPONSES = ["Добро пожаловать!", "Доброго здоровья!", "Здравстуйте", "Рад Вас видеть",
                      "Разрешите Вас приветствовать", "Приветствую",
                      'Да, я бот. Ну и что? Зато я первый, кто здоровается с тобой в чате!']


def greeting(sentence):
    for word in sentence.split():

        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


def bad(sentence):
    RESPONSE = BAD_WORDS
    RESPONSE += ['сам ' + sentence, 'отсоси', 'ты долбаеб', 'ты' + sentence, ]
    for word in sentence.split():
        if word.lower() in BAD_WORDS:
            return random.choice(RESPONSE) + '.'


def response(user_response):
    robo_response = ''

    sent_tokens.append(user_response)

    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')

    tfidf = TfidfVec.fit_transform(sent_tokens)

    vals = cosine_similarity(tfidf[-1], tfidf)

    idx = vals.argsort()[0][-2]

    flat = vals.flatten()

    flat.sort()

    req_tfidf = flat[-2]

    if (req_tfidf == 0):

        robo_response = robo_response + 'Я Вас не понимаю, обратитесь сюда https://zakupki.mos.ru/'

        return robo_response

    else:

        robo_response = robo_response + sent_tokens[idx]

        return robo_response


flag = True


def robo_response(msg):
    user_response = msg

    user_response = user_response.lower()

    if (user_response != 'пока'):

        if (user_response == 'спасибо' or user_response == 'благодарю'):

            return "Обращайтесь.."
        elif (bad(user_response) != None):
            return bad(user_response)

        else:

            if (greeting(user_response) != None):
                return greeting(user_response)

            else:
                return 'не понимаю'


    else:
        return "До свидания, рад был Вам помочь!"
