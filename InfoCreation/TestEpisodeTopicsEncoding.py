# coding:utf-8
import unittest
from EpisodeTopicsEncoding import TopicsTokenizer

class TestTopicsTokenizer(unittest.TestCase):
	
	"""docstring for TestTopicsTokenizer"""

	# Sanity Check Test
	def test_Sanity(self):
		self.assertEqual(True, True)

	def test_TokenizeTerms(self):
		self.assertEqual(
			TopicsTokenizer.tokenize('Thanksgiving, Turkeys, Thawing a Turkey, Dry Brine (Cure), Rubbed Sage, Golden Syrup, Starch'),
			sorted(['Sage', 'Golden', 'Turkeys', 'Syrup', 'a', 'Thawing', 'Turkey', 'Dry', 'Brine', 'Rubbed', 'Starch', 'Thanksgiving', 'Cure']))

		self.assertEqual(
			TopicsTokenizer.tokenize("Bread Pudding, Bread Stalling, Amylose, Half & Half"),
			sorted(["Bread", "Pudding", "Stalling", "Amylose", "Half"]))

	def test_removeStopWords(self):
		self.assertEqual(
			TopicsTokenizer.removeStopWords(TopicsTokenizer.tokenize('Thanksgiving, Turkeys, Thawing a Turkey, Dry Brine (Cure), Rubbed Sage, Golden Syrup, Starch')),
			sorted(['Thanksgiving', 'Turkeys', 'Thawing', 'Turkey', 'Dry', 'Brine', 'Cure', 'Rubbed', 'Sage', 'Golden', 'Syrup', 'Starch']))




if __name__ == '__main__':
	unittest.main()
		