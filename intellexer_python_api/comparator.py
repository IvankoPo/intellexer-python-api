import requests
import json


apikey = ""

class Documents:
    def __init__(self, doc):
        self.__id = doc["id"]
        self.__size = doc["size"]
        self.__title = doc["title"]
        self.__url = doc["url"]
        self.__error = doc["error"]
        self.__sizeFormat = doc["sizeFormat"]

    def get_id(self):
        return self.__id

    def get_size(self):
        return self.__size

    def get_title(self):
        return self.__title

    def get_url(self):
        return self.__url

    def get_error(self):
        return self.__error

    def get_size_format(self):
        return self.__sizeFormat

class Comparator:
    def __init__(self, apikey, text1, text2):
        self.__url = "http://api.intellexer.com/compareText?apikey={0}".format(apikey)
        self.__headers = {'Content-Type': 'application/json; charset=utf-8'}
        self.__data = {'text1': text1, 'text2': text2}
        self.__document = []
        self.__proximity = 0

    def compare_text(self):
        response = requests.post(url=self.__url, data=json.dumps(self.__data), headers=self.__headers)
        self.__proximity = response.json()["proximity"]
        self.__document.append(Documents(response.json()["document1"]))
        self.__document.append(Documents(response.json()["document2"]))

    def get_proximity(self):
        return self.__proximity

    def get_document1(self):
        return self.__document[0]

    def get_doument2(self):
        return self.__document[1]


#---- test

comparator = Comparator(apikey, "another text", "smth text")
comparator.compare_text()
print(comparator.get_proximity())
doc = comparator.get_document1()
print(doc.get_size())
print(doc.get_size_format())