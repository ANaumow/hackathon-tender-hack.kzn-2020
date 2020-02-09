import string
from nltk import word_tokenize
from nltk.corpus import stopwords


def tokenize_ru(text):
    tokens = word_tokenize(text)
    tokens = [i for i in tokens if (i not in string.punctuation)]
    stop_words = stopwords.words('russian')
    stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'в', '—', '–', 'к', 'на', '...'])
    stop_words.remove('как')

    tokens = [i for i in tokens if (i.lower() not in stop_words)]
    tokens = [i.replace("«", "").replace("»", "").replace("\"", "").replace("\'", "").replace("`", "") for i in tokens]
    tokens = filter(lambda x: x is not '', tokens)
    return tokens
