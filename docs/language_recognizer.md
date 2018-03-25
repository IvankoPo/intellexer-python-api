# Language Recognizer
```python
from intellexer_python_api.language_recognizer import RecognizeLanguage
text = "The good thing about this way of building objects of the class is that it works."
key = "your key"

res = RecognizeLanguage().recognize_language(key, text)

array_of_languages = res.get_languages()
for language in array_of_languages:
    print(language.get_language())
    print(language.get_encoding())
    print(language.get_weight())
    print("---")
```