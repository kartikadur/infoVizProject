# coding : utf-8
from bs4 import BeautifulSoup
import csv
from dataManager import DataCollector, DataCleaner
import requests


# File List
filePath = '../Data/'
fileNames = ['goodEatsLinks.csv', 'goodEatsMetadata.csv']
fieldNames = ['Show #', 'Show No.', 'Title', 'Topics', 'Synopsis', 'Original Air Date', 'Transcript', 'Recipes']

dataset = []

# Create FileHandlers
readManager = csv.reader(open(filePath + fileNames[0], 'r'), delimiter=",")
writeManager = csv.DictWriter(open(filePath + fileNames[1], 'w', encoding="utf-8"), delimiter=',', lineterminator='\n', fieldnames=fieldNames)
writeManager.writeheader()

# Create Data Handler
dataCollector = DataCollector()
dataCleaner = DataCleaner()

# Read data from file and iterate through url links to get article data
for row in readManager:
	# get the metadata
	# row[0] = "EA1408"
	# row[2] = "http://www.goodeatsfanpage.com/season14/ea1408h.htm"
	if row[0] == "EASP04H" or row[0] == "EA1115" or row[0] == "EA0921" or row[0] == "EA0915" or row[0] == "EA1H18" or row[0] == "EA1A09":
		# These are being avoided for the time being, and may need to be added manually
		# responseObj = dataCollector.SendHTTPRequest(row[2])
		# continue
		responseObj = open(filePath + row[0] + ".htm", 'r')
		responseObj = responseObj.read()
	else :
		responseObj = dataCollector.MakeHTTPRequest(row[2])
	

	# clean the data before storage
	# print(responseObj.encode('utf-8'))

	# Article Content
	content = dataCleaner.ConvertHTMLToUnicode(responseObj)
	dataset = dataCleaner.ParseDataWithBeautifulSoup(content)


	# To normalize headers when adding to the csv file
	if 'Recipe from Transcript' in dataset and 'Recipes' not in dataset:
		dataset['Recipes'] = dataset.pop('Recipe from Transcript')
	elif 'Recipe from Transcript' in dataset and 'Recipes' in dataset:
		dataset.pop('Recipe from Transcript')

	# Write 'Show #', 'Show No.', 'Title', 'Topics', 'Synopsis', 'Original Air Date', 'Transcript', 'Recipes' to file
	writeManager.writerow(dataset)
	print(row[0]," done!")
	# break