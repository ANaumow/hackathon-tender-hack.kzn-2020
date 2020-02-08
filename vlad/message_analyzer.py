from nltk.stem.snowball import SnowballStemmer
import pymorphy2
import tokenizer
import operator

from naumow.dao import Dao

stemmer = SnowballStemmer("russian")


def get_response(message):
    lst = tokenizer.tokenize_ru(message)
    keywords = []
    for word in lst:
        # stemmed = stemmer.stem(word)
        lemma = pymorphy2.MorphAnalyzer().parse(word)[0].normal_form
        keywords.append(lemma)
    #print(keywords)
    return find_the_most_suitable_answer(set(keywords))


#    return set(keywords)


def find_the_most_suitable_answer(keywords):
    dao = Dao()
    answers = dao.get_dictionary()
    #print(answers)
    value_list = {}
    i = 0
    while i < 166:
        value_list[i] = 0
        i += 1
    for keyword in keywords:
        #print(keyword)
        for answer in answers:
            #print(answer)
            if answers[answer].count(keyword) == 1:
                value_list[answer] += 1
    return sorted(value_list.items(), key=operator.itemgetter(1))[len(value_list) - 1][0]
