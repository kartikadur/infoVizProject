# coding: utf-8
import re
from datetime import datetime

"""
class variables
- episodeID
- showID
- episodeNumber
- seasonNumber
- seasonEpisodeNumber
- Title
- Topic --> store as list (use nltk?)
- Synopsis --> use nltk?
- Original Air date (currently for canada, would the US one be better?)
- Recipes -> store as list
- transcriptID
- transcriptContent

"""

class Episode(object):
	
	"""docstring for Episode"""
	
	def __init__(self, showTitle):
		super(Episode, self).__init__()
		self.showTitle = showTitle

	def setEpisodeID(self, episodeID):
		self.episodeID = episodeID
		self.setSeasonNumber()
		self.setSeasonEpisodeNumber()
		self.setShowID()

	def setShowID(self):
		# self.setEpisodeObjectID = str(self.showSeason).zfill(zFillNumber) + 
		self.showID = str(self.seasonNumber).zfill(2) + str(self.seasonEpisodeNumber).zfill(2)

	def setSeasonEpisodeNumber(self):
		eid = self.episodeID[4:6]
		if eid:
			self.seasonEpisodeNumber = int(eid.strip())
		else :
			self.seasonEpisodeNumber = None
		
	def setSeasonNumber(self):
		sid = self.episodeID[2:4].strip()
		if sid == "SP":
			self.seasonNumber = 15
		elif sid == "1A":
			self.seasonNumber = 1
		elif sid == "1B":
			self.seasonNumber = 2
		elif sid == "1C":
			self.seasonNumber = 3
		elif sid == "1D":
			self.seasonNumber = 4
		elif sid == "1E":
			self.seasonNumber = 5
		elif sid == "1F":
			self.seasonNumber = 6
		elif sid == "1G":
			self.seasonNumber = 7
		elif sid == "1H":
			self.seasonNumber = 8
		elif sid and int(sid) >= 9 and int(sid) <= 14:
			self.seasonNumber = int(sid)
		else :
			self.seasonNumber = None

	def setEpisodeNumber(self, showNo):
		self.episodeNumber = re.sub(r"(st|nd|rd|th)$", "", showNo, flags=re.I)

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




