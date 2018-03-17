import requests


"""
    Объект Sentences хранит в себе все продложения
    get(index) вернет предложение(объект Sentence) под номером index
    gets вернет список предложений(объектов Sentence)
"""
class Sentences:
    def __init__(self, res):
        self.__sentences = []
        for i in res["sentences"]:
            self.__sentences.append(Sentence(i))

    def get(self, index):
        return self.__sentences[index]

    def gets(self):
        return self.__sentences

"""
    Объект Text хранит в себе свойства Content, beginOffset, endOffset
    и может их отдавать соответствующим методом
    Если loadSentences = False Все поля инициализирую None
 """
class Text:
    def __init__(self, text):
        if text is not None:
            self.__content = text["content"]
            self.__beginOffset = text["beginOffset"]
            self.__endOffset = text["endOffset"]
        else:
            self.__content = None
            self.__beginOffset = None
            self.__endOffset = None

    def get_content(self):
        if self.__content is None:
            return "null"
        else:
            return self.__content

    def get_begin_offset(self):
        if self.__beginOffset is None:
            return "null"
        else:
            return self.__beginOffset

    def get_end_offset(self):
        if self.__endOffset is None:
            return "null"
        else:
            return self.__endOffset

"""
    Объект Token хранит в себе объект Text и может его отдать,
    и свойтсва partOfSpeechTag, lemma
 """
class Token:
    def __init__(self, token):
        self.__text = Text(token["text"])
        self.__partOfSpeechTag = token["partOfSpeechTag"]
        self.__lemma = token["lemma"]

    def get_text(self):
        return self.__text

    def get_part_of_speech_tag(self):
        return self.__partOfSpeechTag

    def get_lemma(self):
        if self.__lemma is None:
            return "null"
        else:
            return self.__lemma


"""
    Класс Relation имеет поля: subject, verb, object, adverbialPhrase и соответствующие методы доступа к этим полям
"""
class Relation:
    def __init__(self, relation):
        self.__subject = relation["subject"]
        self.__verb = relation["verb"]
        self.__object = relation["object"]
        self.__adverbialPhrase = relation["adverbialPhrase"]

    def get_subject(self):
        return self.__subject

    def get_verb(self):
        return self.__verb

    def get_object(self):
        return self.__object

    def get_adverbialPhrase(self):
        return self.__adverbialPhrase

"""
    Объект предложение хранит в себе объект Text и список объектов Token
"""
class Sentence:
    def __init__(self, t):
        # или здесь сделать null
        self.__tokens = []
        self.__relations = []
        self.__text = Text(t["text"])
        if t["tokens"] is not None:
            for i in t["tokens"]:
                self.__tokens.append(Token(i))
        if t["relations"] is not None:
            for i in t["relations"]:
                self.__relations.append(Relation(i))

    def get_tokens(self):
        return self.__tokens

    def get_text(self):
        return self.__text

    def get_relations(self):
        return self.__relations

"""
    Главный класс
    Конфигурирует запрос
    Метод analyzeText начинает анализ и возвращает объект Sentences
"""
class LinguisticProcessor:
    def __init__(self, apikey, load_sentences=False, load_tokens=False, load_relations=False):
        self.url = "http://api.intellexer.com/analyzeText?apikey={0}&loadSentences={1}&loadTokens={2}&loadRelations={3}"\
                    .format(apikey, load_sentences, load_tokens, load_relations)
        self.__sent = {}

    def analyze_text(self, text):
        response = requests.post(url=self.url, data=text)
        self.__sent = Sentences(response.json())
        return self.__sent




# ==================== Test

api_key = ""
text = "I stayed here on a 2 night business trip. Excellent location to the airport \
        and the hotel runs a free shuttle bus to the airport."

linguisticProcessor = LinguisticProcessor(api_key, True, True, False)
result = linguisticProcessor.analyze_text(text)
sentences = result.gets()
for sentence in sentences:
    print(sentence.get_text().get_content())
    tokens = sentence.get_tokens()
    for token in tokens:
        print("Токен - " + token.get_text().get_content() + " lemma - " + token.get_lemma())

