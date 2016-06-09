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
	
	def __init__(self, showTitle):
		super(Episode, self).__init__()
		self.showTitle = showTitle

	def setShowID(self, showID):
		self.showID = showID
		self.setShowSeason()
		self.setSeasonShowNumber()


	def setSeasonShowNumber(self):
		eid = self.showID[4:6]
		if eid:
			self.seasonShowNumber = int(eid.strip())
		else :
			self.seasonShowNumber = None
		
	def setShowSeason(self):
		sid = self.showID[2:4].strip()
		if sid == "SP":
			self.showSeason = 15
		elif sid == "1A":
			self.showSeason = 1
		elif sid == "1B":
			self.showSeason = 2
		elif sid == "1C":
			self.showSeason = 3
		elif sid == "1D":
			self.showSeason = 4
		elif sid == "1E":
			self.showSeason = 5
		elif sid == "1F":
			self.showSeason = 6
		elif sid == "1G":
			self.showSeason = 7
		elif sid == "1H":
			self.showSeason = 8
		elif sid and int(sid) >= 9 and int(sid) <= 14:
			self.showSeason = int(sid)
		else :
			self.showSeason = None

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

	def addTranscript(self, content):
		self.transcriptContent = content




