import requests


class NaturalLanguageInterface:
    def convert_query_to_bool(self, apikey, text):
        url = "http://api.intellexer.com/convertQueryToBool?"\
              "apikey={0}".format(apikey)
        response = requests.post(url, data=text)
        return response.text

# --- Example

key = ""
text = "How to increase an integration density in semiconductor memory device?"
res = NaturalLanguageInterface().convert_query_to_bool(key, text)
print(res)