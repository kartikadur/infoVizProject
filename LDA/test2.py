# coding : utf8
# imports
import csv
from nltk.tokenize import RegexpTokenizer, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from gensim import corpora, models



# code
# FileHandling setup
filePath = ['../Data']
fileName = ['goodEatsData.csv']
fileHandler = csv.reader(open('/'.join([filePath[0],fileName[0]]),'r', encoding='utf-8'), delimiter=',')

# Tokenization setup
tokenizer = RegexpTokenizer(r'\w+')

# StopWords setup
stop_words = set(stopwords.words('english'))

# Stemming setup
stemmer = PorterStemmer()

# tempvars
# count = 0
texts = []

for line in fileHandler:
	# print(line[0].encode('utf-8'),line[1].encode('utf-8'))
	tokens = tokenizer.tokenize(line[1].lower())
	stopped_tokens = [i for i in tokens if i not in stop_words and len(i) > 2]
	stemmed_tokens = [stemmer.stem(i) for i in stopped_tokens]
	texts.append(stemmed_tokens)
	# print([i.encode('utf-8') for i in stemmed_tokens])
	# count += 1
	# if count > 3:
	# 	break

# Dictionary with IDs and frequencies
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# LDA Modelling
ldamodel = models.ldamodel.LdaModel(corpus, num_topics = 3, id2word = dictionary, passes = 20)

print(ldamodel.print_topics(num_topics=3, num_words=1))
print(ldamodel.print_topics(num_topics=3, num_words=2))
print(ldamodel.print_topics(num_topics=3, num_words=3))
print(ldamodel.print_topics(num_topics=3, num_words=4))
# print(ldamodel.print_topic())