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

	# Check for air date
	def test_toCheckEpisodeForOriginalAirDate(self):
		self.ep.addAirDate("02.10.2011")
		self.assertEqual(self.ep.airDate, "2011-02-10T00:00:00")

		self.ep.addAirDate("7.11.2001")
		self.assertEqual(self.ep.airDate, "2001-07-11T00:00:00")

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
		self.assertEqual(self.ep.seasonNumber, 10)

		self.ep.setEpisodeID("EASP06H")
		self.assertEqual(self.ep.seasonNumber, 15)

		self.ep.setEpisodeID("EA1G02")
		self.assertEqual(self.ep.seasonNumber, 7)

		self.ep.setEpisodeID("")
		self.assertEqual(self.ep.seasonNumber, None)

	def test_toCheckEpisodeForSeasonEpisodeNumber(self):
		self.ep.setEpisodeID("EA1004H")
		self.assertEqual(self.ep.seasonEpisodeNumber, 4)

		self.ep.setEpisodeID("EASP06H")
		self.assertEqual(self.ep.seasonEpisodeNumber, 6)

		self.ep.setEpisodeID("EA1G02")
		self.assertEqual(self.ep.seasonEpisodeNumber, 2)

		self.ep.setEpisodeID("")
		self.assertEqual(self.ep.seasonEpisodeNumber, None)

	def test_AddingEpisodeTranscript(self):
		self.ep.addTranscript("This is some placeholder text")
		self.assertEqual(self.ep.transcriptContent, "This is some placeholder text")

	def test_toCheckEpisodeAddsEpisodeObjectID(self):
		self.ep.setEpisodeID("EA1004H")
		self.assertEqual(self.ep.showID, '1004')

		self.ep.setEpisodeID("EASP06H")
		self.assertEqual(self.ep.showID, '1506')

		self.ep.setEpisodeID("EA1G02")
		self.assertEqual(self.ep.showID, '0702')



	
if __name__ == '__main__':
	unittest.main()

