from nltk.stem.snowball import SnowballStemmer
import pymorphy2
import operator


import vlad.word_filter as spellchecker
from naumow.dao import Dao
from vlad import tokenizer

stemmer = SnowballStemmer("russian")


def get_response(message):
    lst = tokenizer.tokenize_ru(message)
    keywords = []
    for word in lst:
        checked = spellchecker.correct(word)
        # stemmed = stemmer.stem(word)
        lemma = pymorphy2.MorphAnalyzer().parse(checked)[0].normal_form
        keywords.append(lemma)
    print(keywords)
    return find_the_most_suitable_answer(set(keywords))


#    return set(keywords)


def find_the_most_suitable_answer(keywords):
    dao = Dao()
    answers = dao.get_dictionary()
    #print(answers)
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
            #print("Sss" + str(value_list[answer]) + str(len(answers[answer]) * 1.0))
            value_list[answer] = value_list[answer] / (len(answers[answer]) * 1.0)
            #print(value_list[answer])
        #print(dao.execute("select `text` from hack.`key` where `answer_id` = " + str(answer)))

    return sorted(value_list.items(), key=operator.itemgetter(1))[len(value_list) - 1][0]
