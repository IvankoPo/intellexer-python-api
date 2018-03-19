import requests
import json

apikey = ""

"""
    Хранит результат срвнения
"""
class CompareResult:
    def __init__(self, result):
        self.__proximity = result["proximity"]
        self.__document = []
        self.__document.append(Documents(result["document1"]))
        self.__document.append(Documents(result["document2"]))

    def get_proximity(self):
        return self.__proximity

    def get_document1(self):
        return self.__document[0]

    def get_doument2(self):
        return self.__document[1]


"""
    представляет обьект документ и методы доступа к его свойствам 
"""
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

"""
    Класс Comparator
    Имеет три метда для сравнения
    text - text
    url - url
    url - file
"""
class Comparator:

    def compare_text(self, apikey, text1, text2):
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        data = {'text1': text1, 'text2': text2}
        url = "http://api.intellexer.com/compareText?apikey={0}".format(apikey)
        response = requests.post(url=url, data=json.dumps(data), headers=headers)
        return CompareResult(response.json())

    def compare_urls(self, apikey, url1, url2):
        url = "http://api.intellexer.com/compareUrls?apikey={0}&url1={1}&url2={2}".format(apikey, url1, url2)
        response = requests.get(url)
        return CompareResult(response.json())

    def compare_url_with_file(self, apikey, url, file):
        url = "http://api.intellexer.com/compareUrlwithFile?apikey={0}&fileName=file.txt&url={1}".format(apikey, url)
        files = {"file1": file}
        response = requests.post(url, files=files)
        return CompareResult(response.json())

#--- test


comparator = Comparator().compare_url_with_file(apikey, "https://www.infoplease.com/people"\
                                                        "/who2-biography/barack-obama", open("obama.txt", "rb"))
print(comparator.get_proximity())
doc = comparator.get_document1()
print(doc.get_url())