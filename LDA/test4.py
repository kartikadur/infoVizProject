# encoding : utf-8

import csv
import nltk
from nltk.tokenize import RegexpTokenizer
import re
from gensim import corpora, models
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet, stopwords

# tokenizer setup
tokenizer = RegexpTokenizer(r'\w+')

# lemmatizer setup
lemmatizer = WordNetLemmatizer()

# stopwords setup
sWords = set(stopwords.words('english'))

# FileHandling setup
filePath = ['../Data']
fileName = ['goodEatsData.csv']
fileHandler = csv.reader(open('/'.join([filePath[0],fileName[0]]),'r', encoding='utf-8'), delimiter=',')

# Pattern setup for regex matcher
is_noun = re.compile(r"^NN.{0,2}")
is_verb = re.compile(r"^VB.?")
is_adjective = re.compile(r"^JJ.?")
is_adverd = re.compile(r"^RB.?")

# Extra vars for use
# This List stores list of words from each document after tokenization, stopping, stemming, and pos_tagging
texts = [] 
count = 0

# Check Tag function
def check_tag(tag_name):
	if is_noun.match(tag_name) or is_verb.match(tag_name) or is_adjective.match(tag_name) or is_adverd.match(tag_name) :
		return True
	else :
		return False

# Convert pos type to wordnet type
def pos_to_wn(pos_type):
	if is_noun.match(pos_type):
		return wordnet.NOUN
	elif is_verb.match(pos_type):
		return wordnet.VERB
	elif is_adjective.match(pos_type):
		return wordnet.ADJ
	elif is_adverd.match(pos_type):
		return wordnet.ADV
	else :
		return ''

# NLTK bangers and mash
for line in fileHandler:
	tokens = tokenizer.tokenize(line[1].lower())
	stopped_tokens = [token for token in tokens if token not in sWords and len(token) > 2]
	tagged_tokens = nltk.pos_tag(stopped_tokens)
	lemmatized_tokens = [lemmatizer.lemmatize(i, pos_to_wn(tag)) for i, tag in tagged_tokens if check_tag(tag)]
	texts.append(lemmatized_tokens)
	break


# print([i.encode('utf-8') for text in texts for i in text])

# LDA meat and potatoes
dictionary = corpora.Dictionary(texts)
text_corpus = [dictionary.doc2bow(text) for text in texts]

# LDA Modelling
ldamodel = models.ldamodel.LdaModel(text_corpus, num_topics = 5, id2word = dictionary, passes = 500)

print(ldamodel.print_topics(num_topics=5, num_words=1))
print(ldamodel.print_topics(num_topics=5, num_words=2))
print(ldamodel.print_topics(num_topics=5, num_words=3))
print(ldamodel.print_topics(num_topics=5, num_words=4))

'''
Example output #1
[(0, '0.001*longer'), (1, '0.001*longer'), (2, '0.001*longer'), (3, '0.036*chocolate'), (4, '0.001*longer')]
[(0, '0.001*longer + 0.001*link'), (1, '0.001*longer + 0.001*link'), (2, '0.001*longer + 0.001*link'), (3, '0.036*chocolate + 0.008*dark'), (4, '0.001*longer + 0.001*link')]
[(0, '0.001*handy + 0.001*bitter + 0.001*enrobe'), (1, '0.001*handy + 0.001*bitter + 0.001*enrobe'), (2, '0.001*handy + 0.001*bitter + 0.001*enrobe'), (3, '0.036*chocolate + 0.008*dark + 0.008*go'), (4, '0.001*handy + 0.001*bitter + 0.001*enrobe')]
[(0, '0.001*handy + 0.001*bitter + 0.001*enrobe + 0.001*shout'), (1, '0.001*handy + 0.001*bitter + 0.001*enrobe + 0.001*shout'), (2, '0.001*handy + 0.001*bitter + 0.001*enrobe + 0.001*shout'), (3, '0.036*chocolate + 0.008*dark + 0.008*go + 0.007*cocoa'), (4, '0.001*handy + 0.001*bitter + 0.001*enrobe + 0.001*shout')]
[Finished in 49.8s]

Example output #2
[(0, '0.001*exceed'), (1, '0.001*exceed'), (2, '0.001*exceed'), (3, '0.036*chocolate'), (4, '0.001*exceed')]
[(0, '0.001*exceed + 0.001*attorney'), (1, '0.001*exceed + 0.001*attorney'), (2, '0.001*exceed + 0.001*attorney'), (3, '0.036*chocolate + 0.008*dark'), (4, '0.001*exceed + 0.001*attorney')]
[(0, '0.001*capture + 0.001*fond + 0.001*lucy'), (1, '0.001*capture + 0.001*fond + 0.001*lucy'), (2, '0.001*capture + 0.001*fond + 0.001*lucy'), (3, '0.036*chocolate + 0.008*dark + 0.008*go'), (4, '0.001*capture + 0.001*fond + 0.001*lucy')]
[(0, '0.001*capture + 0.001*fond + 0.001*lucy + 0.001*story'), (1, '0.001*capture + 0.001*fond + 0.001*lucy + 0.001*story'), (2, '0.001*capture + 0.001*fond + 0.001*lucy + 0.001*story'), (3, '0.036*chocolate + 0.008*dark + 0.008*go + 0.007*cocoa'), (4, '0.001*capture + 0.001*fond + 0.001*lucy + 0.001*story')]
[Finished in 48.5s]

Example output #3
[(0, '0.001*dismantle'), (1, '0.001*dismantle'), (2, '0.036*chocolate'), (3, '0.001*dismantle'), (4, '0.001*dismantle')]
[(0, '0.001*dismantle + 0.001*contend'), (1, '0.001*dismantle + 0.001*contend'), (2, '0.036*chocolate + 0.008*dark'), (3, '0.001*dismantle + 0.001*contend'), (4, '0.001*dismantle + 0.001*contend')]
[(0, '0.001*invisible + 0.001*barely + 0.001*blade'), (1, '0.001*invisible + 0.001*barely + 0.001*blade'), (2, '0.036*chocolate + 0.008*dark + 0.008*go'), (3, '0.001*invisible + 0.001*barely + 0.001*blade'), (4, '0.001*invisible + 0.001*barely + 0.001*blade')]
[(0, '0.001*invisible + 0.001*barely + 0.001*blade + 0.001*discern'), (1, '0.001*invisible + 0.001*barely + 0.001*blade + 0.001*discern'), (2, '0.036*chocolate + 0.008*dark + 0.008*go + 0.007*cocoa'), (3, '0.001*invisible + 0.001*barely + 0.001*blade + 0.001*discern'), (4, '0.001*invisible + 0.001*barely + 0.001*blade + 0.001*discern')]
[Finished in 87.4s]

'''

