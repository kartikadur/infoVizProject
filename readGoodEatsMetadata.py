# coding:utf-8
from bs4 import BeautifulSoup
import csv
from dataManager import DataCollector, DataCleaner
from fileManager import fileManager
import requests


# File List
filePath = ''
fileNames = ['goodEatsLinks.csv', 'goodEatsMetadata.csv']
fieldNames = ['Show #', 'Show No.', 'Title', 'Topics', 'Synopsis', 'Original Air Date', 'Transcript', 'Recipes']
dataset = []

# Create FileHandlers
readManager = fileManager(fileNames[0])
readManager.openFile()
# writeManager = fileManager(fileNames[1])
# writeManager.openFile('wb')
writeManager = csv.DictWriter(open(fileNames[1], 'w'), delimiter=',', lineterminator='\n', fieldnames=fieldNames)
writeManager.writeheader()

# Create Data Handler
dataCollector = DataCollector()
dataCleaner = DataCleaner()

# Read data from file and iterate through url links to get article data
for row in readManager.getRows():
	# get the metadata
	# responseObj = dataCollector.MakeHTTPRequest(row[2])
	responseObj = dataCollector.MakeHTTPRequest("http://www.goodeatsfanpage.com/Season5/EA1E09.htm")

	# print row[2]

	# clean the data before storage

	# Article Content
	content = dataCleaner.ConvertHTMLToUnicode(responseObj['content'])
	dataset = dataCleaner.ParseDataWithBeautifulSoup(content)

	# print dataset


	# content = dataCleaner.CleanDataUsingRegex('<[^>]*>', '', content)
	# content = dataCleaner.CleanDataUsingRegex('[\xc2\xa0]+', '', content)
	# content = dataCleaner.CleanDataUsingRegex('[\\n]+', '', content)
	# content = dataCleaner.CleanDataUsingRegex('[\s]+', ' ', content)
	# content = content.encode('utf-8')

	# Article Title
	# title = dataCleaner.ConvertHTMLToUnicode(responseObj['title'].decode('utf-8'))
	# title = dataCleaner.CleanDataUsingRegex(r'(?i)[\s]+Tran[c]?script', '', title)
	# title = title.encode('utf-8')

	# Write EpisodeCode, EpisodeSeason, EpisodeTitle, EpisodeContent to file
	writeManager.writerow(dataset)

	break

readManager.closeFile()