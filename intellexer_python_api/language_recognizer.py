import requests


"""
    Объект language
    Содержит в себе поля:
    - language
    - encoding
    - weight
"""


class Language:
    def __init__(self, json):
        self.__language = json["language"]
        self.__encoding = json["encoding"]
        self.__weight = json["weight"]

    def get_language(self):
        return self.__language

    def get_encoding(self):
        return self.__encoding

    def get_weight(self):
        return self.__weight


"""
    Результат запроса
    содержит в себе массив languages
"""


class RecognizeLanguageResult:
    def __init__(self, json):
        self.__language = []
        if json["languages"] is not None:
            for lan in json["languages"]:
                self.__language.append(Language(lan))

    def get_languages(self):
        return self.__language


"""
    Через этот класс делаем запрос
    Метод recognize_language:
    apikey - ключ
    text - текст
"""


class RecognizeLanguage:
    def recognize_language(self, apikey, text):
        url = "http://api.intellexer.com/recognizeLanguage?"\
              "apikey={0}".format(apikey)
        response = requests.post(url, data=text)
        return RecognizeLanguageResult(response.json())


