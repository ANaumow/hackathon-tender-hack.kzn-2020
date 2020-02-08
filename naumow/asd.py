from nltk.stem.snowball import SnowballStemmer
'''import pymorphy2
import vlad.tokenizer as tokenizer

inputs = input();

lst = tokenizer.tokenize_ru(inputs)
keywords = []
for word in lst:
    # stemmed = stemmer.stem(word)
    lemma = pymorphy2.MorphAnalyzer().parse(word)[0].normal_form
    keywords.append(lemma)

print(set(keywords))'''