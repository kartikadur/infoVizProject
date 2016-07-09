# encoding : utf8
import csv
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
from gensim import corpora, models


# FileHandling setup
filePath = ['../Data']
fileName = ['goodEatsData.csv']
fileHandler = csv.reader(open('/'.join([filePath[0],fileName[0]]),'r', encoding='utf-8'), delimiter=',')

# Pattern setup for regex matcher
pattern = re.compile(r"^NN.*|RB.?|JJ.?|VB.?")

# Tokenizer setup
tokenizer = RegexpTokenizer(r'\w+')

# Stopwords setup
stop_words = set(stopwords.words("english"))

# Stemmer setup
stemmer = PorterStemmer()

# Extra vars for use
# This List stores list of words from each document after tokenization, stopping, stemming, and pos_tagging
texts = [] 
count = 0

# Check Tag function
def check_tag(tag_name):
	if pattern.match(tag_name) :
		return True
	else :
		return False



for line in fileHandler:
	tokens = tokenizer.tokenize(line[1].lower())
	stopped_tokens = [i for i in tokens if i not in stop_words and len(i) > 2]
	tagged_tokens = nltk.pos_tag(stopped_tokens)
	stemmed_tokens = [stemmer.stem(i) for i, tag in tagged_tokens if check_tag(tag)]
	texts.append(stemmed_tokens)
	count += 1
	if count > 3:
		break

# print(stemmed_tokens)

# This is where the LDA magic happens
# Dictionary with IDs and frequencies
dictionary = corpora.Dictionary(texts)
text_corpus = [dictionary.doc2bow(text) for text in texts]

# LDA Modelling
ldamodel = models.ldamodel.LdaModel(text_corpus, num_topics = 5, id2word = dictionary, passes = 250)

print(ldamodel.print_topics(num_topics=5, num_words=1))
print(ldamodel.print_topics(num_topics=5, num_words=2))
print(ldamodel.print_topics(num_topics=5, num_words=3))
print(ldamodel.print_topics(num_topics=5, num_words=4))

'''
Example output #1
[(0, '0.018*chocol'), (1, '0.000*plethora'), (2, '0.000*exact'), (3, '0.010*heat'), (4, '0.027*noodl')]
[(0, '0.018*chocol + 0.007*time'), (1, '0.000*plethora + 0.000*exact'), (2, '0.000*exact + 0.000*slightli'), (3, '0.010*heat + 0.010*smoke'), (4, '0.027*noodl + 0.009*rice')]
[(0, '0.018*chocol + 0.007*time + 0.006*go'), (1, '0.000*plethora + 0.000*exact + 0.000*slightli'), (2, '0.000*exact + 0.000*slightli + 0.000*instanc'), (3, '0.010*heat + 0.010*smoke + 0.010*barbecu'), (4, '0.027*noodl + 0.009*rice + 0.008*sauc')]
[(0, '0.018*chocol + 0.007*time + 0.006*go + 0.006*minut'), (1, '0.000*plethora + 0.000*exact + 0.000*slightli + 0.000*instanc'), (2, '0.000*exact + 0.000*slightli + 0.000*instanc + 0.000*plethora'), (3, '0.010*heat + 0.010*smoke + 0.010*barbecu + 0.009*right'), (4, '0.027*noodl + 0.009*rice + 0.008*sauc + 0.007*go')]

Example output #2
[(0, '0.009*pie'), (1, '0.027*noodl'), (2, '0.000*symbol'), (3, '0.034*chocol'), (4, '0.010*heat')]
[(0, '0.009*pie + 0.008*turkey'), (1, '0.027*noodl + 0.009*rice'), (2, '0.000*symbol + 0.000*involv'), (3, '0.034*chocol + 0.008*dark'), (4, '0.010*heat + 0.010*smoke')]
[(0, '0.009*pie + 0.008*turkey + 0.008*giblet'), (1, '0.027*noodl + 0.009*rice + 0.008*sauc'), (2, '0.000*symbol + 0.000*involv + 0.000*countri'), (3, '0.034*chocol + 0.008*dark + 0.007*go'), (4, '0.010*heat + 0.010*smoke + 0.010*barbecu')]
[(0, '0.009*pie + 0.008*turkey + 0.008*giblet + 0.007*minut'), (1, '0.027*noodl + 0.009*rice + 0.008*sauc + 0.007*go'), (2, '0.000*symbol + 0.000*involv + 0.000*countri + 0.000*fast'), (3, '0.034*chocol + 0.008*dark + 0.007*go + 0.006*cocoa'), (4, '0.010*heat + 0.010*smoke + 0.010*barbecu + 0.009*right')]

Example output #3
[(0, '0.011*noodl'), (1, '0.018*chocol'), (2, '0.000*midnight'), (3, '0.000*war'), (4, '0.000*darkest')]
[(0, '0.011*noodl + 0.008*heat'), (1, '0.018*chocol + 0.007*time'), (2, '0.000*midnight + 0.000*particular'), (3, '0.000*war + 0.000*scatter'), (4, '0.000*darkest + 0.000*aisl')]
[(0, '0.011*noodl + 0.008*heat + 0.008*go'), (1, '0.018*chocol + 0.007*time + 0.006*go'), (2, '0.000*midnight + 0.000*particular + 0.000*concoct'), (3, '0.000*war + 0.000*scatter + 0.000*saucepan'), (4, '0.000*darkest + 0.000*aisl + 0.000*sell')]
[(0, '0.011*noodl + 0.008*heat + 0.008*go + 0.007*meat'), (1, '0.018*chocol + 0.007*time + 0.006*go + 0.006*minut'), (2, '0.000*midnight + 0.000*particular + 0.000*concoct + 0.000*possess'), (3, '0.000*war + 0.000*scatter + 0.000*saucepan + 0.000*garnish'), (4, '0.000*darkest + 0.000*aisl + 0.000*sell + 0.000*disappear')]

'''
