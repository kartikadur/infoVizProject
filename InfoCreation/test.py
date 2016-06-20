# coding : utf-8
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import json
import csv

anotherShow = 'another show'

readManager = csv.reader(open('../Data/goodEatsData.csv', 'r', encoding='utf-8'), delimiter=',')

for line in readManager:
	if 'Dark Chocolate'.lower() in line[1].lower():
		print ('Yes in show ', line[0])

	# break
