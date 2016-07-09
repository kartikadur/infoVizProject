import numpy as np
import lda
import lda.datasets
import matplotlib.pyplot as plt

X = lda.datasets.load_reuters()
# print("type(X): {}".format(type(X)))
# print("shape: {}\n".format(X.shape))

vocab = lda.datasets.load_reuters_vocab()
# print("type(X): {}".format(type(vocab)))
# print("shape: {}\n".format(len(vocab)))

titles = lda.datasets.load_reuters_titles()
# print("type(X): {}".format(type(titles)))
# print("shape: {}\n".format(len(titles)))

doc_id = 0
word_id = 3117

# print("doc id: {} word id : {}".format(doc_id, word_id))
# print("-- count: {}".format(X[doc_id,word_id]))
# print("-- word: {}".format(vocab[word_id]))
# print("-- doc: {}".format(titles[doc_id]))

model = lda.LDA(n_topics = 20, n_iter = 500, random_state = 1)
model.fit(X)

topic_word = model.topic_word_
# print("type(topic_word): {}".format(type(topic_word)))
# print("shape: {}".format(topic_word.shape))

# # sum of probability of words
# for n in range(5):
# 	sum_pr = sum(topic_word[n,:])
# 	print("topic: {} sum: {}".format(n, sum_pr))

# # top 5 words for each topic by probability
# n = 5
# for i, topic_dist in enumerate(topic_word):
# 	topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n+1): -1]
# 	print('*Topic {}\n - {}'.format(i, ' '.join(topic_words)))

'''Document Topic'''
# document topic probability
doc_topic = model.doc_topic_
# print("type(doc_topic): {}".format(type(doc_topic)))
# print("shape: {}".format(doc_topic.shape))

# # Normalized document topic
# for n in range(5):
# 	sum_pr = sum(doc_topic[n,:])
# 	print("document: {} sum: {}".format(n, sum_pr))

# # Most probable document topic
# for n in range(10):
# 	topic_most_pr = doc_topic[n].argmax()
# 	print("doc: {} topic: {}\n{}...".format(n, topic_most_pr, titles[n][:50]))

'''Plotting datasets'''
# Setting the style
try:
	plt.style.use('ggplot')
except :
	pass

# # matplotlib goes here, try bokeh next time
# f, ax = plt.subplots(5, 1, figsize=(8,6), sharex=True)
# for i, k in enumerate([0,4,9,14,19]):
# 	ax[i].stem(topic_word[k,:], linefmt = 'b-', markerfmt='bo', basefmt='w-')
# 	ax[i].set_xlim(-50, 4350)
# 	ax[i].set_ylim(0, 0.1)
# 	ax[i].set_ylabel("Prob")
# 	ax[i].set_title("topic {}".format(k))

# ax[4].set_xlabel("word")

# plt.tight_layout()
# plt.show()

# topic distribution by document for each of the 20 topics
f, ax = plt.subplots(5, 1, figsize = (8,6), sharex = True)
for i, k in enumerate([1,3,4,8,9]):
	ax[i].stem(doc_topic[k,:], linefmt = 'r-', markerfmt='ro', basefmt='w-')
	ax[i].set_xlim(-1, 21)
	ax[i].set_ylim(0, 1)
	ax[i].set_ylabel("Prob")
	ax[i].set_title("Document {}".format(k))

ax[4].set_xlabel("Topic")

plt.tight_layout()
plt.show()
