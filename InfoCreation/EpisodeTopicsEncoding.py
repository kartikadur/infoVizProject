# coding:utf-8
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

tokenizer = RegexpTokenizer(r'\w+')
stop_words = set(stopwords.words('english'))

class TopicsTokenizer():

	"""docstring for TopicsTokenizer"""

	@staticmethod
	def tokenize(stringToTokenize):
		wordList = set(tokenizer.tokenize(stringToTokenize))
		return sorted(list(wordList))

	@staticmethod
	def removeStopWords(listWithStopWords):
		wordList = []
		for word in listWithStopWords:
			if word not in stop_words and len(word) > 2:
				wordList.append(word)

		# print(wordList)
		return wordList