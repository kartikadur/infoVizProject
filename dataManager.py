# coding: utf-8
from HTMLParser import HTMLParser
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
		return parsedResponse

class DataCleaner:

	"""docstring for DataCleaner"""

	def __ini__(self):
		return

	def ConvertHTMLToUnicode(self, data):
		parserHTML = HTMLParser()
		if data :
			if isinstance(data, str):
				data.decode('utf-8')
			return parserHTML.unescape(data)
		else :
			return None

	def CleanDataUsingRegex(self, regex, replace, data):
		# future check for list or string and process accordingly
		if regex and data :
			return re.sub(regex, replace, data)
		else :
			return None