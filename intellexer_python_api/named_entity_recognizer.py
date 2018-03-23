import requests


class Type:
    def __init__(self, json):
        self.__possible_values = {
            0: "Unknown",
            1: "Person",
            2: "Organization",
            3: "Location",
            4: "Title",
            5: "Position",
            6: "Age",
            7: "Date",
            8: "Duration",
            9: "Nationality",
            10: "Event",
            11: "Url",
            12: "MiscellaneousLocation"
            }
        self.__name = self.__possible_values[json]
        self.__type = json

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type


class RelationsTree:
    def __init__(self, json):
        self.__children = []
        self.__count = json["count"]
        self.__dependency = json["dependency"]
        self.__sentence_ids = json["sentenceIds"]
        self.__text = json["text"]
        self.__type = json["type"]
        for i in json["children"]:
            self.__children.append(RelationsTree(i))

    def get_children(self):
        return self.__children

    def get_count(self):
        return self.__count

    def get_dependency(self):
        return self.__dependency

    def get_sentence_ids(self):
        return self.__sentence_ids

    def get_text(self):
        return self.__text

    def get_type(self):
        return self.__type


class Entity:
    def __init__(self, json):
        self.__sentence_ids = json["sentenceIds"]
        self.__type = Type(json["type"])
        self.__wc = json["wc"]
        self.__text = json["text"]

    def get_sentence_ids(self):
        return self.__sentence_ids

    def get_type(self):
        return self.__type

    def get_wc(self):
        return self.__wc

    def get_text(self):
        return self.__text


class Document:
    def __init__(self, json):
        self.__id = json["id"]
        self.__size = json["size"]
        self.__title = json["title"]
        self.__url = json["url"]
        self.__error = json["error"]
        self.__size_format = json["sizeFormat"]

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
        return self.__size_format


class NamedEntityRecognizerResult:
    def __init__(self, json):
        self.__document = None
        self.__entities = []
        self.__sentences = None
        self.__relations_tree = None
        if json["entities"] is not None:
            for entity in json["entities"]:
                self.__entities.append(Entity(entity))
        if json["sentences"] is not None:
            self.__sentences = json["sentences"]
        if json["relationsTree"] is not None:
            self.__relations_tree = RelationsTree(json["relationsTree"])
        if json["document"] is not None:
            self.__document = Document(json["document"])

    def get_document(self):
        return self.__document

    def get_entities(self):
        return self.__entities

    def get_sentences(self):
        return self.__sentences

    def get_relations_tree(self):
        return self.__relations_tree


class NamedEntityRecognizer:
    def recognize_from_url(self, apikey, url, load_named_entities=False,
                            load_relations_tree=False, load_sentences=False):
        url = "http://api.intellexer.com/recognizeNe?" \
              "apikey={0}" \
              "&loadNamedEntities={1}" \
              "&loadRelationsTree={2}" \
              "&loadSentences={3}" \
              "&url={4}".format(apikey, load_named_entities, load_relations_tree,
                                load_sentences, url)
        response = requests.get(url)
        return NamedEntityRecognizerResult(response.json())

    def recognize_from_file(self, apikey, file, file_name="1.txt",
                            load_named_entities=False,
                            load_relations_tree=False, load_sentences=False, file_size=1233):
        url = "http://api.intellexer.com/recognizeNeFileContent?"\
              "apikey={0}"\
              "&fileName={1}"\
              "&fileSize={2}"\
              "&loadNamedEntities={3}"\
              "&loadRelationsTree={4}"\
              "&loadSentences={5}".format(apikey, file_name, file_size, load_named_entities,
                                          load_relations_tree, load_sentences)
        response = requests.post(url, files={file_name: file})
        return NamedEntityRecognizerResult(response.json())

    def recognize_from_text(self, apikey, text, load_named_entities=False,
                            load_relations_tree=False, load_sentences=False):
        url = "http://api.intellexer.com/recognizeNeText?"\
              "apikey={0}"\
              "&loadNamedEntities={1}"\
              "&loadRelationsTree={2}"\
              "&loadSentences={3}".format(apikey, load_named_entities, load_relations_tree, load_sentences)
        response = requests.post(url, data=text)
        return NamedEntityRecognizerResult(response.json())

# --- Example1


uri = "https://www.intellexer.com/about_us.html"
key = ""
f = open("obama.txt", "rb")
res = NamedEntityRecognizer().recognize_from_file(key, f, load_sentences=True, load_named_entities=True, load_relations_tree=True)
entities = res.get_entities()
for entity in entities:
    print(entity.get_text())
    print(entity.get_type().get_name())
    print(entity.get_wc())
    print("----")


# --- Example2


text = "Eyal Shaked was appointed General Manager of the Optical Networks Division in October 2005."
result = NamedEntityRecognizer().recognize_from_text(key, text, load_sentences=True, load_named_entities=True, load_relations_tree=True)

result = result.get_entities()
for entity in result:
    print(entity.get_text())
    print(entity.get_type().get_name())
    print("----")




