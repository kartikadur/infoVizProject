# coding: utf-8
from html.parser import HTMLParser
from bs4 import BeautifulSoup
from collections import defaultdict
import re
import json
import requests

class DataCollector:
	
	"""docstring for GoodEatsData"""

	# Readability API
	__readability = {
		"base" : "https://readability.com/api/content/",
		"version" : "v1",
		"apiType" : ["parser", "confidence"],
		"token" : "0355da835a55164bb30c1f566a4a69b79b6e1b74"
	}


	def __init__(self):
		return

	def MakeHTTPRequest(self, targetURL):
		httpRequestString = self.__readability["base"] + self.__readability["version"] + "/" + self.__readability["apiType"][0] + "?url=" + targetURL + "&token=" + self.__readability["token"]
		responseObj = requests.get(httpRequestString)
		parsedResponse = json.loads(responseObj.text)
		# print parsedResponse
		return parsedResponse['content']

	def SendHTTPRequest(self, targetURL):
		responseObj = requests.get(targetURL)
		# print responseObj
		# print responseObj.text.encode('utf-8')
		return responseObj.text

class DataCleaner:

	"""docstring for DataCleaner"""

	def __ini__(self):
		pass

	def ConvertHTMLToUnicode(self, data):
		parserHTML = HTMLParser()
		if data :
			return parserHTML.unescape(data)
		else :
			return None

	def CleanDataUsingRegex(self, regex, replace, data):
		# future check for list or string and process accordingly
		if regex and data :
			return re.sub(regex, replace, data)
		else :
			return None

	def CleanDataUsingRegexList(self, regex, replace, data = []):
		tempdata = []
		if regex and isinstance(data, list):
			for d in data:
				tempdata.append(re.sub(regex, replace, d))
			return tempdata
		else :
			return None

	def ParseDataWithBeautifulSoup(self, data):
		# pass

		soup = BeautifulSoup(data, "html.parser")
		pattern = re.compile('^(?i)Title|Transcript|Show|Original Air Date|Topics|Synopsis|Recipes$')

		# Find all HTML code within 'table' tags
		tables = soup.find_all("table")

		tableData = []
		datasets = defaultdict()
		# search for 'title' in table
		# Skip table if it cannot be found in table
		for table in tables:
			# if(table.find('Title')): print table
			for row in table.find_all("tr"):
				dataset = []
				for td in row.find_all("td"):
					dataset.append(td.get_text())
				tableData.append(dataset)

		for item in tableData:
			if pattern.match(item[0]):
				item[0] = item[0].encode('utf-8')
				item[1] = item[1].encode('utf-8')
				item = self.CleanDataUsingRegexList('[\xc2\xa0]+', '', item)
				item = self.CleanDataUsingRegexList('[\\n]+', '', item)
				item = self.CleanDataUsingRegexList('[\s]+', ' ', item)
				datasets[item[0]] = item[1]

		# print datasets
		return datasets

if __name__ == '__main__':
	dataCollector = DataCollector()
	responseObj = dataCollector.MakeHTTPRequest("http://www.goodeatsfanpage.com/Season13/EASP04H.htm")
	print(responseObj)