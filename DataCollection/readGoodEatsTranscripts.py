# coding:utf-8
import csv
from dataManager import DataCollector, DataCleaner
import requests


# File List
filePath = '../Data/'
fileNames = ['goodEatsLinks.csv', 'goodEatsData.csv']

# Create FileHandlers
readManager = csv.reader(open(filePath + fileNames[0], 'r'), delimiter=",")
writeManager = csv.writer(open(filePath + fileNames[1], 'w', encoding="utf-8"), delimiter=",", lineterminator='\n')

# Create Data Handler
dataCollector = DataCollector()
dataCleaner = DataCleaner()

# Read data from file and iterate through url links to get article data
for row in readManager:
	# get the data
	# responseObj = dataCollector.MakeHTTPRequest('http://www.goodeatsfanpage.com/Season5/Crepe/CrepeTranscript.htm')
	responseObj = dataCollector.MakeHTTPRequest(row[3])

	# clean the data before storage
	# Article Content
	content = dataCleaner.ConvertHTMLToUnicode(responseObj)
	content = dataCleaner.CleanDataUsingRegex('<[^>]*>', '', content)
	content = dataCleaner.CleanDataUsingRegex(u'\u00A0', ' ', content)
	content = dataCleaner.CleanDataUsingRegex('[\\n]+', ' ', content)
	content = dataCleaner.CleanDataUsingRegex('[\s]+', ' ', content)

	# Write EpisodeCode, EpisodeContent to file
	writeManager.writerow([row[0], content])
	print(row[0] + " done!")
	# break
	