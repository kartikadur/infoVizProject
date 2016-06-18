from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import json

ps = PorterStemmer()
stop_words = set(stopwords.words("english"))

fp = open("../DataCleaned/jsonOut.json", "r")
text = fp.read()

print(text[200:1000])


