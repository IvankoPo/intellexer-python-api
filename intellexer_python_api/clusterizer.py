import requests


"""
    Класс ClusterizeResult хранит реультат 
"""


class ClusterizeResult:
    def __init__(self, obj):
        self.__concept_tree = ConceptTree(obj["conceptTree"])
        self.__sentences = []
        for i in obj["sentences"]:
            self.__sentences.append(i)

    def get_concept_tree(self):
        return self.__concept_tree

    def get_sentences(self):
        return self.__sentences


"""
    Clusterizer
    имеет 3 метода
    по названию методов все понятно
"""


class Clusterizer:
    def clusterize_url(self, apikey, url, load_sentences, fullTextTrees):
        self.__url = "http://api.intellexer.com/clusterize?apikey={0}"\
                     "&fullTextTrees={1}&loadSentences={2}" \
                     "&url={3}"\
                     "&useCache=false&wrapConcepts=false".format(apikey, fullTextTrees, load_sentences, url)
        response = requests.get(self.__url)
        return ClusterizeResult(response.json())

    def clusterize_text(self, apikey, text, load_sentences, fullTextTrees):
        self.__url = "http://api.intellexer.com/clusterizeText?apikey={0}"\
                     "&fullTextTrees={1}&loadSentences={2}" \
                     "&useCache=false&wrapConcepts=false".format(apikey, fullTextTrees, load_sentences)
        response = requests.post(self.__url, data=text)
        return ClusterizeResult(response.json())

    def clusterize_file(self, apikey, file, load_sentences, fullTextTrees):
        self.__url = "http://api.intellexer.com/clusterizeFileContent?"\
                     "apikey={0}"\
                     "&fileName=2.txt&fullTextTrees={1}&loadSentences={2}".format(apikey, fullTextTrees, load_sentences)
        file = {"file1": file}
        response = requests.post(self.__url, files=file)
        return ClusterizeResult(response.json())


"""
    Предствалние обьекта ConceptTree
    И методы доступа к его свойствам 
"""


class ConceptTree:
    def __init__(self, obj):
        self.__children = []
        self.__main_phrase = obj["mp"]
        self.__sentence_ids = []
        self.__status = obj["st"]
        self.__text = obj["text"]
        self.__weight = obj["w"]
        for i in obj["sentenceIds"]:
            self.__sentence_ids.append(i)
        for i in obj["children"]:
            self.__children.append(ConceptTree(i))

    def get_children(self):
        return self.__children

    def get_main_pharse(self):
        return self.__main_phrase

    def get_sentence_ids(self):
        return self.__sentence_ids

    def get_status(self):
        return self.__status

    def get_text(self):
        return self.__text

    def get_weight(self):
        return self.__weight
