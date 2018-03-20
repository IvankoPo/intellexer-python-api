import json
import re
import requests

class Sentiment:
    def __init__(self, json):
        self.__authon = json["author"]
        self.__dt = json["dt"]
        self.__id = json["id"]
        self.__title = json["title"]
        self.__weight = json["w"]

    def get_author(self):
        return self.__authon

    def get_dt(self):
        return self.__dt

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_weight(self):
        return self.__weight

class Sentence:
    def __init__(self, json):
        self.__patern_for_pos = "<pos[^<>]*?>\s*(.*?)<\/pos>"
        self.__patern_for_obj = "<obj>(.*?)<\/obj>"
        self.__patern_for_neg = "<pos[^<>]*?>\s*(.*?)<\/pos>"
        self.__sid = json["sid"]
        self.__text = json["text"]
        self.__weight = json["w"]
        self.__positive_words = re.findall(self.__patern_for_pos, self.__text)
        self.__negative_words = re.findall(self.__patern_for_neg, self.__text)
        self.__sentiment_object = re.findall(self.__patern_for_obj, self.__text)

    def get_positive_words(self):
        return self.__positive_words

    def get_negative_words(self):
        return self.__negative_words

    def get_sentiment_object(self):
        return self.__sentiment_object

    def get_sid(self):
        return self.__sid

    def get_text(self):
        return self.__text

    def get_weight(self):
        return self.__weight

class Opinions:
    def __init__(self, json):
        self.__children = []
        self.__f = json["f"]
        self.__rs = json["rs"]
        self.__t = json["t"]
        self.__w = json["w"]
        if json["children"] is not None:
            for i in json["children"]:
                self.__children.append(Opinions(i))

    def get_children(self):
        return self.__children

    def get_f(self):
        return self.__f

    def get_rs(self):
        return self.__rs

    def get_t(self):
        return self.__t

    def get_weight(self):
        return self.__w


class SentimentAnalyzerResult:
    def __init__(self, json):
        self.__sentiment_count = json["sentimentsCount"]
        self.__ontology = json["ontology"]
        self.__sentences = []
        if json["opinions"] is not None:
            self.__opinions = Opinions(json["opinions"])
        else:
            self.__opinions = None
        self.__sentiments = []
        if json["sentences"] is not None:
            for sentence in json["sentences"]:
                self.__sentences.append(Sentence(sentence))
        if json["sentiments"] is not None:
            for sentence in json["sentiments"]:
                self.__sentiments.append(Sentiment(sentence))

    def get_sentiment_count(self):
        return self.__sentiment_count

    def get_ontology(self):
        return self.__ontology

    def get_sentences(self):
        return self.__sentences

    def get_opinions(self):
        return self.__opinions

    def get_sentiments(self):
        return self.__sentiments


"""
    {
    "sentimentsCount": 1,
    "ontology": "hotels",
    "sentences": null,
    "opinions": {
        "children": [],
        "f": 0,
        "rs": [],
        "t": null,
        "w": 0
    },
    "sentiments": [
        {
            "author": null,
            "dt": null,
            "id": "1",
            "title": null,
            "w": 0
        }
    ]
} 
"""


class SentimentAnalyzer:
    def sentiment_analyzer_ontologies(self, apikey):
        url = "http://api.intellexer.com/sentimentAnalyzerOntologies?apikey={0}".format(apikey)
        respose = requests.get(url)
        return respose.json()

    def analyze_sentiments(self, apikey, data, load_sentences, ontology=None):
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        if ontology is not None:
            url = "http://api.intellexer.com/analyzeSentiments?apikey={0}&loadSentences={1}&ontology={2}"\
                .format(apikey, load_sentences, ontology)
        else:
            url = "http://api.intellexer.com/analyzeSentiments?apikey={0}&loadSentences={1}" \
                .format(apikey, load_sentences)
        response = requests.post(url=url, data=json.dumps(data), headers=headers)
        return SentimentAnalyzerResult(response.json())

key = "07ce7c6a-5b21-4d2b-9bd6-8f8d11ce0480"


data = [{"id": "1", "text": "Hello, world! It's been a great day"},
        {"id": "2", "text": "Intellexer Summarizer has an unique feature."}]

result = SentimentAnalyzer().analyze_sentiments(key, data, load_sentences=True, ontology="Hotels")
print(result.get_sentiment_count())
print(result.get_sentiments()[0].get_weight())
array_sentences = result.get_sentences()
for sentence in array_sentences:
    print(sentence.get_text() + " weight = " + str(sentence.get_weight()))
    print(sentence.get_positive_words())




