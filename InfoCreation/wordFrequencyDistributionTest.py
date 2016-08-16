# encoding : utf-8

import csv
import simplejson as json
from nltk import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import OrderedDict, defaultdict

import pygal


filePath = ['../Data','../DataCleaned']
inputFileName = ['goodEatsMetadata.csv', 'goodEatsData.csv']
outputFileName = ['testNetwork.json']

# File Handlers / File Pointers
readMetadata = csv.DictReader(open('/'.join([filePath[0], inputFileName[0]]), 'r'), delimiter=',')
readData = csv.reader(open('/'.join([filePath[0], inputFileName[1]]), 'r', encoding='utf-8'), delimiter=',')

tokenized_word_set = defaultdict()
tokenizer = RegexpTokenizer(r'\w+')
stop_words = set(stopwords.words('english'))

personal_stopwords = set(('well', 'scene', 'know', 'got', 'okay', 'like', 'let', 'going', 'get', 'kind', 'really', 'way', 'lot', 'could', 'around'))
# 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'zero',

# print(stop_words)
# print(personal_stopwords)

tokenized_and_stopped_wordlist = []
for data in readData:
	for word in tokenizer.tokenize(data[1]):
		if word.lower() not in stop_words and word.lower() not in personal_stopwords and len(word) > 2:
			tokenized_and_stopped_wordlist.append(word.lower())
			# counts word frequency manually
			# if word.lower() in tokenized_word_set:
			# 	tokenized_word_set[word.lower()] += 1
			# else :
			# 	tokenized_word_set[word.lower()] = 1


fdist = FreqDist(tokenized_and_stopped_wordlist)
linechart = pygal.Bar()
for token, count in fdist.most_common(100):
	linechart.add(token, count)

linechart.render(is_unicode=True)

