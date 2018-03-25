import requests


class NaturalLanguageInterface:
    def convert_query_to_bool(self, apikey, text):
        url = "http://api.intellexer.com/convertQueryToBool?"\
              "apikey={0}".format(apikey)
        response = requests.post(url, data=text)
        return response.text
