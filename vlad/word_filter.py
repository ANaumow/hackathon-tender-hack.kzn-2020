import requests


def correct(word):
    params = {'text': word, 'lang': "ru"}
    r = requests.get('http://speller.yandex.net/services/spellservice.json/checkText', params=params)

    if r.status_code == 200:
        try:
            if r.json():
                out = r.json()[0]
                variants = [v for v in out['s']]
                return variants[0]
            else:
                return word
        except:
            return word
            print('spellchecker')


