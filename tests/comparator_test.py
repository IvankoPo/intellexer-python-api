from intellexer_python_api.comparator import Comparator

apikey = "07ce7c6a-5b21-4d2b-9bd6-8f8d11ce0480"
text = "The products, information,"\
       " and other content provided by this seller are provided for informational purposes only."

url = "https://www.infoplease.com/people"\
      "/who2-biography/barack-obama"

file = open("obama.txt", "rb")

comparator = Comparator().compare_url_with_file(apikey, url, file=file , filename="obama.txt")
print(comparator.get_proximity())
doc = comparator.get_document1()
print(doc.get_url())
doc = comparator.get_doument2()
print(doc.get_title())

comparator = Comparator().compare_text(apikey, text1=text, text2=text)
print(comparator.get_proximity())