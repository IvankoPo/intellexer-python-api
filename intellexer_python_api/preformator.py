import requests


"""
    Результат запроса
    поля:
    - structure
    - topics
    - language
    - language_id
    - input_size
    - size
    - text
"""


class ParseResult:
    def __init__(self, json):
        self.__structure = json["structure"]
        self.__topics = []
        self.__language = json["lang"]
        self.__language_id = json["langId"]
        self.__input_size = json["inputSize"]
        self.__size = json["size"]
        self.__text = json["text"]
        if json["topics"] is not None:
            for topic in json["topics"]:
                self.__topics.append(topic)

    def get_structure(self):
        return self.__structure

    def get_topics(self):
        return self.__topics

    def get_language(self):
        return self.__language

    def get_language_id(self):
        return self.__language_id

    def get_input_size(self):
        return self.__input_size

    def get_size(self):
        return self.__size

    def get_text(self):
        return self.__text


class Preformator:
    def supported_document_structures(self, apikey):
        url = "http://api.intellexer.com/supportedDocumentStructures?"\
              "apikey={0}".format(apikey)
        response = requests.get(url)
        return response.json()

    def supported_document_topics(self, apikey):
        url = "http://api.intellexer.com/supportedDocumentTopics?"\
              "apikey={0}".format(apikey)
        response = requests.get(url)
        return response.json()

    def parse(self, apikey, url):
        api_url = "http://api.intellexer.com/parse?"\
                  "apikey={0}&"\
                  "url={1}".format(apikey, url)
        response = requests.get(api_url)
        return ParseResult(response.json())

    def parse_file_content(self, apikey, file, filename):
        url = "http://api.intellexer.com/parseFileContent?"\
              "apikey={0}&"\
              "fileName={1}".format(apikey, filename)
        f = {filename: file}
        response = requests.post(url, files=f)
        return ParseResult(response.json())


