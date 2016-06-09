# coding: utf-8
import re
from datetime import datetime

"""
class variables
1. showID
2. showNumber
3. Title
4. Topic --> store as list (use nltk?)
5. Synopsis --> use nltk?
6. Original Air date (currently for canada, would the US one be better?)
7. Recipes -> store as list

"""

class Episode(object):
	
	"""docstring for Episode"""
	
	def __init__(self, showID, showTitle):
		super(Episode, self).__init__()
		
		self.showID = showID
		self.showTitle = showTitle

	def setShowNumber(self, showNo):
		self.showNumber = re.sub(r"(st|nd|rd|th)$", "", showNo, flags=re.I)

	def addTopics(self, topics):
		self.topicList = topics.strip().split(", ")

	def addRecipes(self, recipes):
		self.recipeList = []
		tempRecipes = re.compile(r"\s?[0-9][\)|\.]\s?").split(recipes.strip())
		for recipe in tempRecipes:
			if recipe and not re.match('[\w\W]*none[\w\W]*.', recipe, re.IGNORECASE):
				self.recipeList.append(recipe)

	def addAirDate(self, airDate):
		self.airDate = datetime.strptime(airDate, "%m.%d.%Y").isoformat()

	def addTranscriptID(self, transcriptID):
		self.transcriptID = transcriptID




