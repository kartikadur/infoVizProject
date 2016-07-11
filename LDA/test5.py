from nltk.corpus import wordnet

syns = wordnet.synsets('programs')

# # synset
# print(syns[0].name())

# # just the word
# print(syns[0].lemmas()[0].name())

# # definition
# print(syns[0].definition())

# # example
# print(syns[0].examples())

# synonyms = []
# antonyms = []

# for syn in wordnet.synsets('good'):
# 	for l in syn.lemmas():
# 		# print("l: {}".format(l))
# 		synonyms.append(l.name())
# 		if l.antonyms():
# 			antonyms.append(l.antonyms()[0].name())

# print(set(synonyms))
# print(set(antonyms))

# w1 = wordnet.synset('ship.n.01')
# w2 = wordnet.synset('boat.n.01')

# print(w1.wup_similarity(w2))

# w1 = wordnet.synset('ship.n.01')
# w2 = wordnet.synset('car.n.01')

# print(w1.wup_similarity(w2))

# w1 = wordnet.synset('ship.n.01')
# w2 = wordnet.synset('cat.n.01')

# print(w1.wup_similarity(w2))

w1 = wordnet.synset('writing_desk.n.01')
w2 = wordnet.synset('raven.n.01')

print('writing desk vs. raven comparison : {}'.format(w1.wup_similarity(w2)))

w1 = wordnet.synset('sun.n.01')
w2 = wordnet.synset('cactus.n.01')

print('sun vs. cactus comparison : {}'.format(w1.wup_similarity(w2)))