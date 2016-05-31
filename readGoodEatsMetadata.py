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
	# row[0] = "EA1E05"
	# row[2] = "http://www.goodeatsfanpage.com/Season12/EA1E05.htm"
	if row[0] == "EASP04H" or row[0] == "EA1115":
		responseObj = dataCollector.SendHTTPRequest(row[2])
	elif row[0] == "EA0921" or row[0] == "EA0915" or row[0] == "EA1H18" :
		# These are being avoided for the time being, and may need to be added manually
		# responseObj = dataCollector.SendHTTPRequest(row[2])
		continue
	# elif row[0] == "EA1E05" :
	# 	responseObj = dataCollector.MakeHTTPRequest(row[2])
	else :
		responseObj = dataCollector.MakeHTTPRequest(row[2])
	

	# clean the data before storage

	# Article Content
	content = dataCleaner.ConvertHTMLToUnicode(responseObj)
	dataset = dataCleaner.ParseDataWithBeautifulSoup(content)

	# To normalize headers when adding to the csv file
	# if row[0] == "EA1F05" or row[0] == "EA1E05":
	# 	dataset['Recipes'] = dataset.pop('Recipe from Transcript')

	# Write 'Show #', 'Show No.', 'Title', 'Topics', 'Synopsis', 'Original Air Date', 'Transcript', 'Recipes' to file
	writeManager.writerow(dataset)
	print dataset["Show #"] + " done!"

	# break

readManager.closeFile()