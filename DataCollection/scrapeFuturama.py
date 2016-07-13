# encoding : utf-8

from dataManager import DataCollector, DataCleaner
import csv
from bs4 import BeautifulSoup, SoupStrainer
import re

# URL Listings
baseURL = "http://www.imsdb.com"
baseURI = "TV/Futurama.html"
transcriptURI = ["transcripts"]

# storage file
filePath = "../Data"
fileName = "futurama_links.csv"

# File handler for writing data/ links
fileWriter = csv.writer(open('/'.join([filePath,fileName]), 'w', encoding='utf-8'), delimiter=',', lineterminator='\n')

# Data collection using api reader wrapper
dataCollector = DataCollector()
scriptCollector = DataCollector()
content = dataCollector.MakeHTTPRequest('/'.join([baseURL, baseURI]))
datacleaner = DataCleaner()

# Getting the episodes
epCount = 0
for link in BeautifulSoup(content, 'html.parser', parse_only=SoupStrainer('a')):
	# print(link)
	if link.has_attr('href') and "TV%20Transcripts" in link['href']:
		epCount += 1
		linkURL = datacleaner.CleanDataUsingRegex(r'%20', ' ', link['href'])
		epName = link.contents[0]

		# Based on linkURL get the transcript url
		# look for table with class script-details
		soup = BeautifulSoup(datacleaner.ConvertHTMLToUnicode(scriptCollector.SendHTTPRequest(linkURL)), 'html.parser')
		for transcriptLink in soup.find('table', { 'class' : 'script-details' }).find_all('a'):
			if transcriptLink.has_attr('href') and 'transcripts' in transcriptLink['href']:
				transcriptLinkURL = ''.join([baseURL,transcriptLink['href']])
		try:
			# write individual rows to the csv file
			# each row contains the episode number, episode name, metadata link
			fileWriter.writerow([epCount, epName, linkURL, transcriptLinkURL])
		except Exception as e:
			print(str(e))

		print("Completed Episode {}".format(epName))
		# # Single loop for Testing purposes
		# break
