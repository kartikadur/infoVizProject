import unittest
from EpisodeClass import Episode
from datetime import datetime

class TestEpisode(unittest.TestCase):

	"""docstring for TestEpisode"""
	def setUp(self):
		self.ep = Episode('dummyID', 'dummyTitle')

	# Sanity check test
	def test_Sanity(self):
		self.assertEqual(True, True)

	# Check Episode Constructor
	def test_EpisodeForID(self):
		self.assertEqual(self.ep.showID, "dummyID")

	def test_EpisodeForTitle(self):
		self.assertEqual(self.ep.showTitle, "dummyTitle")


	def test_ShowNumberRemovesOrdinalEnding(self):
		# check removes 'st' from 'x1st'
		self.ep.setShowNumber('21st')
		self.assertEqual(self.ep.showNumber, '21')
		self.ep.setShowNumber('1ST')
		self.assertEqual(self.ep.showNumber, '1')

		# check removes 'nd' from 'x2nd'
		self.ep.setShowNumber('92nd')
		self.assertEqual(self.ep.showNumber, '92')

		# check removes 'rd' from 'x3rd'
		self.ep.setShowNumber('33rd')
		self.assertEqual(self.ep.showNumber, '33')
		
		# check removes 'th' from 'x[4-9]th'
		self.ep.setShowNumber('24th')
		self.assertEqual(self.ep.showNumber, '24')

	def test_CreateListFromAddedTopics(self):
		self.ep.addTopics("Turkeys, Brining, Electric Knives, Stuffing, Basting, Probe Thermometers")
		self.assertEqual(self.ep.topicList, ["Turkeys","Brining","Electric Knives","Stuffing","Basting","Probe Thermometers"])

	def test_CreateListfromAddedRecipes(self):
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

	def test_EpisodeForOriginalAirDate(self):
		self.ep.addAirDate("02.10.2011")
		self.assertEqual(self.ep.airDate, "2011-02-10T00:00:00")

		self.ep.addAirDate("7.11.2001")
		self.assertEqual(self.ep.airDate, "2001-07-11T00:00:00")

	def test_EpisodeAddsTranscriptID(self):
		self.ep.addTranscriptID("Turn On the Dark")
		self.assertEqual(self.ep.transcriptID, "Turn On the Dark")

		self.ep.addTranscriptID("")
		self.assertEqual(self.ep.transcriptID, "")


	
if __name__ == '__main__':
	unittest.main()

