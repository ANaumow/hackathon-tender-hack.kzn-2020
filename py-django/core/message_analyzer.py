from nltk.stem.snowball import SnowballStemmer
import pymorphy2
import operator

import core.word_filter as spellchecker
from db.dao import Dao
from core import tokenizer
from googletrans import Translator
import core.references as refs

stemmer = SnowballStemmer("russian")
excluded_words = ['эцп', 'эп', 'инн', 'сте', 'фос', 'эм', 'кс', 'окато']
translator = Translator()


def language_handler(message):
    if translator.detect(message).lang == 'en':
        refs.is_en = 1
        return translator.translate(message, src='en', dest='ru').text
    else:
        refs.is_en = 0
        return message


def get_response(message):
    message = language_handler(message)
    lst = tokenizer.tokenize_ru(message)
    keywords = []
    for word in lst:
        if excluded_words.count(word) == 0:
            checked = spellchecker.correct(word)
            lemma = pymorphy2.MorphAnalyzer().parse(checked)[0].normal_form
            keywords.append(lemma)
        else:
            keywords.append(word)
    print(keywords)
    return find_the_most_suitable_answer(set(keywords))


#    return set(keywords)


def find_the_most_suitable_answer(keywords):
    dao = Dao()
    answers = dao.get_dictionary()
    # print(answers)
    value_list = {}
    i = 0
    while i < 500:
        value_list[i] = 0.0
        i += 1

    '''for keyword in keywords:
        #print(keyword)
        for answer in answers:
            #print(answer)
            if answers[answer].count(keyword) == 1:
                value_list[answer] += 1'''

    # print(keyword)
    for answer in answers:
        for keyword in keywords:
            # print(answer)
            if answers[answer].count(keyword) == 1:
                value_list[answer] += 1
        if len(answers[answer]) != 0:
            # print("Sss" + str(value_list[answer]) + str(len(answers[answer]) * 1.0))
            value_list[answer] = value_list[answer] / (len(answers[answer]) * 1.0)
            # print(value_list[answer])
        # print(dao.execute("select `text` from hack.`key` where `answer_id` = " + str(answer)))

    return sorted(value_list.items(), key=operator.itemgetter(1))[len(value_list) - 1][0]
