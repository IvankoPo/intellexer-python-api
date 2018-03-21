import requests

key = ""

url = "https://www.intellexer.com/about_us.html"


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

file = open("Avtobiografia_Poleschuk_Ivan.docx", "rb")


res = Preformator().parse_file_content(key, file, "about.txt")
print(res.get_structure())
print(res.get_input_size())
print(res.get_size())
print(res.get_topics())
print(res.get_text())