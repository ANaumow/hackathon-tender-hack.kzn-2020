from nltk.stem.snowball import SnowballStemmer
import pymorphy2
import vlad.tokenizer as tokenizer

from naumow.dao import Dao


def add_to_bd(key_filename, answer_filename, start_id):
    try:
        key_file = open(key_filename, 'r', encoding="UTF-8")
        answer_file = open(answer_filename, 'r', encoding="UTF-8")

        #key_file_len = len([x for x in key_file.readlines()])
        #answer_file_len = len([x for x in answer_file.readlines()])

        #if key_file_len != answer_file_len:
        #    print("not equal")

        #count = min(key_file_len, answer_file_len)

        for i, keys_line in enumerate(key_file.readlines()):

            #keys_line = key_file.readline()
            answer_line = answer_file.readline()
            dao = Dao()

            stemmer = SnowballStemmer("russian")
            lst = tokenizer.tokenize_ru(keys_line)
            keywords = []
            for word in lst:
                # stemmed = stemmer.stem(word)
                lemma = pymorphy2.MorphAnalyzer().parse(word)[0].normal_form
                keywords.append(lemma)
            #print("keyword " + str(keywords))

            for keyword in keywords:
                sql = "insert into hack.`key`(text, answer_id) values ('" + keyword + "', " + str(i) + ");"
                dao.execute(sql)
            sql = "insert into answer(id, text) values (" + str(i) + ", '" + answer_line + "')"
            dao.execute(sql)
    finally:
        key_file.close()
        answer_file.close()


add_to_bd("input.txt", "output.txt", 0)
