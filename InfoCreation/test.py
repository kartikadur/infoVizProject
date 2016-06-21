# coding : utf-8
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import json
import csv

anotherShow = 'another show'

readManager = csv.DictReader(open('../Data/goodEatsMetadata.csv', 'r', encoding='utf-8'), delimiter=',')

# Getting the appropriate topics for categorization of episodes
# Probably needs stemming and probably other stuff too
count = 0
tokenized_word_set = set()
tokenizer = RegexpTokenizer(r'\w+')
stop_words = set(stopwords.words('english'))

for line in readManager:
	for word in tokenizer.tokenize(line['Topics']):
		if word not in stop_words and len(word) > 2:
			tokenized_word_set.add(word.lower())
	
print(len(tokenized_word_set))
for i in tokenized_word_set:
	print(i.encode('utf-8'))
