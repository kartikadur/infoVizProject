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
	# count += 1
	# if count > 10:
	# 	break


# print([i.encode('utf-8') for text in texts for i in text])

# LDA meat and potatoes
dictionary = corpora.Dictionary(texts)
text_corpus = [dictionary.doc2bow(text) for text in texts]

# LDA Modelling
ldamodel = models.ldamodel.LdaModel(text_corpus, num_topics = 50, id2word = dictionary, passes = 500)

for t, w in ldamodel.print_topics():
	print("Topic #{} : {}".format(t, w))

# print(ldamodel.print_topics(num_topics=50, num_words=2))
# print(ldamodel.print_topics(num_topics=50, num_words=3))
# print(ldamodel.print_topics(num_topics=50, num_words=4))

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

all documents and 100 iterations for 10 starting topics
output
Topic #17 : 0.011*get + 0.010*go + 0.010*well + 0.008*know + 0.008*good + 0.007*make + 0.007*scene + 0.006*water + 0.006*little + 0.006*time
Topic #7 : 0.011*go + 0.010*get + 0.008*good + 0.007*well + 0.007*make + 0.006*scene + 0.006*use + 0.006*know + 0.005*little + 0.005*time
Topic #5 : 0.047*corn + 0.007*meal + 0.007*endosperm + 0.006*get + 0.005*ear + 0.005*kernel + 0.005*make + 0.004*sugar + 0.004*look + 0.004*bread
Topic #13 : 0.029*onion + 0.015*paella + 0.013*rice + 0.007*soup + 0.005*saffron + 0.004*make + 0.004*sweet + 0.004*trick + 0.004*vidalia + 0.004*spanish
Topic #18 : 0.051*elton + 0.020*macaroni + 0.018*cheese + 0.008*noodle + 0.007*marsha + 0.007*casserole + 0.005*mom + 0.004*pasta + 0.004*jefferson + 0.004*egg
Topic #1 : 0.011*get + 0.010*go + 0.009*cake + 0.007*make + 0.007*good + 0.007*cup + 0.007*well + 0.006*little + 0.006*scene + 0.006*use
Topic #0 : 0.009*go + 0.009*get + 0.007*oil + 0.007*well + 0.007*use + 0.006*little + 0.006*good + 0.006*heat + 0.006*make + 0.005*scene
Topic #12 : 0.012*get + 0.011*go + 0.009*water + 0.008*good + 0.007*make + 0.007*well + 0.007*little + 0.007*time + 0.006*salt + 0.006*scene
Topic #4 : 0.018*cream + 0.018*chocolate + 0.016*sugar + 0.012*butter + 0.011*get + 0.011*go + 0.009*ice + 0.008*egg + 0.008*cup + 0.007*make
Topic #19 : 0.000*go + 0.000*get + 0.000*water + 0.000*scene + 0.000*little + 0.000*well + 0.000*know + 0.000*right + 0.000*cup + 0.000*cook
[Finished in 1858.6s]

Output for all documents with 50 categories and 500 iterations
Topic #18 : 0.042*yeast + 0.020*bread + 0.019*rise + 0.016*go + 0.016*roll + 0.014*clam + 0.014*pizza + 0.013*flour + 0.012*dough + 0.011*water
Topic #36 : 0.022*oyster + 0.018*duck + 0.012*bread + 0.010*cup + 0.010*go + 0.008*molasses + 0.008*spf + 0.007*wheat + 0.006*good + 0.006*right
Topic #20 : 0.002*stigma + 0.002*wetland + 0.002*doggedly + 0.002*converted + 0.002*seperate + 0.002*catalogue + 0.002*madagascar + 0.002*lodging + 0.000*get + 0.000*go
Topic #5 : 0.131*corn + 0.045*apple + 0.017*meal + 0.010*kernel + 0.009*maize + 0.009*endosperm + 0.009*ear + 0.008*get + 0.008*husk + 0.007*grain
Topic #1 : 0.041*ounce + 0.037*protein + 0.034*bar + 0.025*fat + 0.021*soy + 0.020*soybean + 0.020*essential + 0.018*acid + 0.015*fiber + 0.014*oil
Topic #7 : 0.016*egg + 0.013*get + 0.011*go + 0.008*little + 0.007*time + 0.007*make + 0.007*good + 0.007*water + 0.007*well + 0.006*scene
Topic #39 : 0.000*get + 0.000*creatures + 0.000*gimbal + 0.000*gilliam + 0.000*addicted + 0.000*guru + 0.000*wahunitashur + 0.000*quantum + 0.000*imitator + 0.000*thy
Topic #31 : 0.037*rice + 0.015*grain + 0.012*risotto + 0.011*cook + 0.010*little + 0.009*cup + 0.009*know + 0.009*amylose + 0.008*go + 0.008*amylopectin
Topic #14 : 0.090*strawberry + 0.061*berry + 0.021*bread + 0.012*can + 0.010*clot + 0.010*radical + 0.009*basket + 0.009*tip + 0.009*macerate + 0.007*electron
Topic #41 : 0.000*get + 0.000*well + 0.000*go + 0.000*thy + 0.000*joist + 0.000*gilliam + 0.000*addicted + 0.000*guru + 0.000*wahunitashur + 0.000*imitator
[Finished in 10970.9s]

'''