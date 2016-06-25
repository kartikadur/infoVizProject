# coding : utf-8
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import OrderedDict, defaultdict
import json
import csv

anotherShow = 'another show'

readManager = csv.DictReader(open('../Data/goodEatsMetadata.csv', 'r', encoding='utf-8'), delimiter=',')

# Getting the appropriate topics for categorization of episodes
# Probably needs stemming and probably other stuff too
count = 0
tokenized_word_set = defaultdict()
tokenizer = RegexpTokenizer(r'\w+')
stop_words = set(stopwords.words('english'))

for line in readManager:
	for word in tokenizer.tokenize(line['Topics']):
		if word not in stop_words and len(word) > 2:
			if word.lower() in tokenized_word_set:
				tokenized_word_set[word.lower()] += 1
			else :
				tokenized_word_set[word.lower()] = 1
	
print(len(tokenized_word_set))
total = 0
count = 0
tempDict = OrderedDict(sorted(tokenized_word_set.items(), key=lambda t: t[1], reverse=True))
for i in tempDict:
	print(i.encode('utf-8'), tempDict[i])
	total += tempDict[i]
	count += 1
	if count >= 20 :
		break
print(total)

# total count of all the words = 1502 (100%)
# total count of top 20 words = 171 (11.38%)