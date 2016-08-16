# coding: utf-8

import re
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bs
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier

# Import labeled training data using pandas
train_data = pd.read_csv("data/labeledTrainData.tsv",
							header=0,delimiter="\t", quoting=3)
test = pd.read_csv("data/testData.tsv", header=0,
					delimiter="\t", quoting=3)

# Retrieve a set of commonly use stop words
stops = set(stopwords.words("english"))

# empty list to hold clean reviews
clean_train_reviews = []
clean_test_reviews = []

# variable to hold number of reviews
num_train_reviews = len(train_data["review"])
num_test_reviews = len(test["review"])

# initialize "CountVectorizer" object, scikit-learn's bag of words tool
vectorizer = CountVectorizer(analyzer = "word",
								tokenizer = None,
								preprocessor = None,
								stop_words = None,
								max_features = 5000)

# Initialize a Random Forest Classifier with 100 trees
forest = RandomForestClassifier(n_estimators = 100)

# --- SECTION: METHODS --- #
# Function to convert raw review data to meaningful texts
def review_to_words(raw_review):

	# remove HTML tags using beautifulsoup
	review_text = bs(raw_review, "html.parser").get_text()

	# remove any characters that are not alphabets
	letters_only = re.sub("[^a-zA-Z]", " ", review_text)

	# convert to lower case and separate into words
	words = letters_only.lower().split()

	# remove stop words from list of words
	meaningful_words = [w for w in words if w not in stops]

	# Return meaningful words as a single sentence separated by spaces
	return(" ".join(meaningful_words))


# --- SECTION: TRAINING DATA --- #

for i in range(0, num_train_reviews):
	clean_train_reviews.append(review_to_words(train_data["review"][i]))
	if (i + 1) % 1000 == 0 :
		print("Completed training review {0} of {1}".format(i+1, num_train_reviews))
	# temp measure to prevent extra long processing times 
	# while testing incomplete program
	# if(i > 9) : break

# CountVectorizer Information
train_data_features = vectorizer.fit_transform(clean_train_reviews).toarray()

vocab = vectorizer.get_feature_names()
# Test print of vocabulary
# print(vocab)
# Test print of vocabulary word count
# dist = np.sum(train_data_features, axis=0)
# for tag, count in zip(vocab, dist):
# 	print(count, tag)

# RandomForestClassifier Information
forest = forest.fit(train_data_features, train_data["sentiment"])

# --- SECTION: TEST DATA --- #

# Check that data shape is 25000 by 2
# print(test.shape)

# Clean the review data from the test dataset
for i in range(0, num_test_reviews):
	clean_test_reviews.append(review_to_words(test["review"][i]))
	if (i + 1) % 1000 == 0 :
		print("Completed review under test {0} of {1}".format(i+1, num_test_reviews))

# Create a bag of words for the data under test
test_data_features = vectorizer.transform(clean_test_reviews)
test_data_features = test_data_features.toarray()

# Random Forest Classifier created earlier on the test data
result = forest.predict(test_data_features)

# create output using pandas dataframe
output = pd.DataFrame( data = {"id":test["id"], "sentiment":result} )

# Create CSV output file using pandas
output.to_csv( "Bag_of_Words_model.csv", index=False, quoting=3)

# --- END FILE --- #