import unittest
from EpisodeClass import Episode
from datetime import datetime

class TestEpisode(unittest.TestCase):

	"""docstring for TestEpisode"""
	def setUp(self):
		self.ep = Episode('dummyTitle')

	# Sanity check test
	def test_Sanity(self):
		self.assertEqual(True, True)

	# Check Episode Constructor
	# def test_EpisodeForID(self):
	# 	self.assertEqual(self.ep.showID, "dummyID")

	# Check for Episode Title
	def test_EpisodeForTitle(self):
		self.assertEqual(self.ep.showTitle, "dummyTitle")


	# Check for Show Number
	def test_toCheckEpisodeNumberRemovesOrdinalEnding(self):
		# check removes 'st' from 'x1st'
		self.ep.setEpisodeNumber('21st')
		self.assertEqual(self.ep.episodeNumber, '21')
		self.ep.setEpisodeNumber('1ST')
		self.assertEqual(self.ep.episodeNumber, '1')

		# check removes 'nd' from 'x2nd'
		self.ep.setEpisodeNumber('92nd')
		self.assertEqual(self.ep.episodeNumber, '92')

		# check removes 'rd' from 'x3rd'
		self.ep.setEpisodeNumber('33rd')
		self.assertEqual(self.ep.episodeNumber, '33')
		
		# check removes 'th' from 'x[4-9]th'
		self.ep.setEpisodeNumber('24th')
		self.assertEqual(self.ep.episodeNumber, '24')

		# Check for xxx(st|nd|rd|th) followed by other text
		self.ep.setEpisodeNumber('199th Note: If the cranberry episode, Cran Opening, had aired in the US during the same season as it was created, this would have been the 200th episode in the USA.')
		self.assertEqual(self.ep.episodeNumber, '199')

	# Check for topics list
	def test_toCreateListFromAddedTopics(self):
		self.ep.addTopics("Turkeys, Brining, Electric Knives, Stuffing, Basting, Probe Thermometers")
		self.assertEqual(self.ep.topicList, ["Turkeys","Brining","Electric Knives","Stuffing","Basting","Probe Thermometers"])

	# Check for recipe list
	def test_toCreateListfromAddedRecipes(self):
		self.ep.addRecipes("1) Beef Tenderloin in Salt Crust 2) Perfect Fingerling Potatoes 3) Salt Roasted Shrimp 4) Sauerkraut")
		self.assertEqual(self.ep.recipeList, ["Beef Tenderloin in Salt Crust","Perfect Fingerling Potatoes","Salt Roasted Shrimp","Sauerkraut"])

		self.ep.addRecipes("1. Dan Dan Noodles 2. Ants in Trees 3. Thai Shrimp Spring Rolls")
		self.assertEqual(self.ep.recipeList, ["Dan Dan Noodles","Ants in Trees","Thai Shrimp Spring Rolls"])

		self.ep.addRecipes("None given at FN.com")
		self.assertEqual(self.ep.recipeList,[])

		self.ep.addRecipes("--none--")
		self.assertEqual(self.ep.recipeList,[])

		self.ep.addRecipes("")
		self.assertEqual(self.ep.recipeList,[])

		self.ep.addRecipes(".")
		self.assertEqual(self.ep.recipeList,[])		

	# Check for air date
	def test_toCheckEpisodeForOriginalAirDate(self):
		self.ep.addAirDate("02.10.2011")
		self.assertEqual(self.ep.airDate, "2011-02-10T00:00:00")

		self.ep.addAirDate("7.11.2001")
		self.assertEqual(self.ep.airDate, "2001-07-11T00:00:00")

		self.ep.addAirDate("07.??.1998: WTTW, Ch. 11, Chicago, IL 07.07.1999: FoodTV")
		self.assertEqual(self.ep.airDate, "1999-07-07T00:00:00")

		self.ep.addAirDate("11.14.1999 (During Season 1)")
		self.assertEqual(self.ep.airDate, "1999-11-14T00:00:00")

		self.ep.addAirDate("12.08.2008 in the US 05.26.2008 (maybe) in Canada")
		self.assertEqual(self.ep.airDate, "2008-12-08T00:00:00")

		self.ep.addAirDate("10.10.2009 at 10:00 pm")
		self.assertEqual(self.ep.airDate, "2009-10-10T00:00:00")

		self.ep.addAirDate("10.26..2009")
		self.assertEqual(self.ep.airDate, "2009-10-26T00:00:00")

	# Check for transcript ID
	def test_toCheckEpisodeForTranscriptID(self):
		self.ep.addTranscriptID("Turn On the Dark")
		self.assertEqual(self.ep.transcriptID, "Turn On the Dark")

		self.ep.addTranscriptID("")
		self.assertEqual(self.ep.transcriptID, "")

	# Check if correct season is set
	def test_toCheckEpisodeForEpisodeID(self):
		self.ep.setEpisodeID("EA1004H")
		self.assertEqual(self.ep.episodeID, "EA1004H")

		# self.ep.setEpisodeID("EASP06H")

		# self.ep.setEpisodeID("EA1G02")

	def test_toCheckEpisodeForSeason(self):
		self.ep.setEpisodeID("EA1004H")
		self.assertEqual(Episode.getSeasonNumber(self.ep.episodeID), 10)

		self.ep.setEpisodeID("EASP06H")
		self.assertEqual(Episode.getSeasonNumber(self.ep.episodeID), 15)

		self.ep.setEpisodeID("EA1G02")
		self.assertEqual(Episode.getSeasonNumber(self.ep.episodeID), 7)

		self.ep.setEpisodeID("")
		self.assertEqual(Episode.getSeasonNumber(self.ep.episodeID), None)

	def test_toCheckEpisodeForSeasonEpisodeNumber(self):
		self.ep.setEpisodeID("EA1004H")
		self.assertEqual(Episode.getSeasonEpisodeNumber(self.ep.episodeID), 4)

		self.ep.setEpisodeID("EASP06H")
		self.assertEqual(Episode.getSeasonEpisodeNumber(self.ep.episodeID), 6)

		self.ep.setEpisodeID("EA1G02")
		self.assertEqual(Episode.getSeasonEpisodeNumber(self.ep.episodeID), 2)

		self.ep.setEpisodeID("")
		self.assertEqual(Episode.getSeasonEpisodeNumber(self.ep.episodeID), None)

	def test_AddingEpisodeTranscript(self):
		self.ep.addTranscript("This is some placeholder text")
		self.assertEqual(self.ep.transcriptContent, "This is some placeholder text")

	def test_toCheckEpisodeAddsEpisodeObjectID(self):
		self.ep.setEpisodeID("EA1004H")
		self.assertEqual(Episode.getShowID(self.ep.episodeID), '1004')

		self.ep.setEpisodeID("EASP06H")
		self.assertEqual(Episode.getShowID(self.ep.episodeID), '1506')

		self.ep.setEpisodeID("EA1G02")
		self.assertEqual(Episode.getShowID(self.ep.episodeID), '0702')



	
if __name__ == '__main__':
	unittest.main()

