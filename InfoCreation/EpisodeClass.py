# coding: utf-8
import re
from EpisodeTopicsEncoding import TopicsTokenizer
from datetime import datetime
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

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
		self.seasonNumber = self.getSeasonNumber(episodeID)
		self.seasonEpisodeNumber = self.getSeasonEpisodeNumber(episodeID)

	@staticmethod
	def getShowID(episodeID = None):
		return str(Episode.getSeasonNumber(episodeID)).zfill(2) + str(Episode.getSeasonEpisodeNumber(episodeID)).zfill(2)

	@staticmethod
	def getSeasonEpisodeNumber(episodeID = None):
		if not isinstance(episodeID, str) :
			episodeID = episodeID.decode('utf-8')
		eid = episodeID[4:6].strip()
		if eid:
			return int(eid.strip())
		else :
			return None
		
	@staticmethod
	def getSeasonNumber(episodeID = None):
		if not isinstance(episodeID, str) :
			episodeID = episodeID.decode('utf-8')
		sid = episodeID[2:4].strip()
		if sid == "SP":
			return 15
		elif sid == "1A":
			return 1
		elif sid == "1B":
			return 2
		elif sid == "1C":
			return 3
		elif sid == "1D":
			return 4
		elif sid == "1E":
			return 5
		elif sid == "1F":
			return 6
		elif sid == "1G":
			return 7
		elif sid == "1H":
			return 8
		elif sid and int(sid) >= 9 and int(sid) <= 14:
			return int(sid)
		else :
			return None

	def setEpisodeNumber(self, showNo):
		self.episodeNumber = re.sub(r"(st|nd|rd|th).*$", "", showNo, flags=re.I)

	def addTopics(self, topics):
		self.topicList = TopicsTokenizer.removeStopWords(TopicsTokenizer.tokenize(topics))

	def addRecipes(self, recipes):
		self.recipeList = []
		tempRecipes = re.compile(r"\s?[0-9][\)|\.]\s?").split(recipes.strip())
		for recipe in tempRecipes:
			if recipe and not re.match('[\w\W]*none[\w\W]*.', recipe, re.IGNORECASE) and not re.match('\.', recipe):
				self.recipeList.append(recipe)

	def addAirDate(self, airDate):
		
		# Create Pattern to check for dates in the format mm.dd.yyyy
		pattern = re.compile('[\d]{1,2}\.[\d]{1,2}\.[\d]{4}')

		# Remove any extra periods so that format matches mm.dd.yyyy
		airDate = re.sub('[\.]+', '.', airDate)
		
		tempDate = pattern.search(airDate)
		if tempDate :
			self.airDate = datetime.strptime(tempDate.group(), "%m.%d.%Y").isoformat()
		else :
			self.airDate = None

	def addTranscriptID(self, transcriptID):
		self.transcriptID = transcriptID

	def addTranscript(self, content):
		self.transcriptContent = content




