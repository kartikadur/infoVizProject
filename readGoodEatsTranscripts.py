import requests
from bs4 import BeautifulSoup, SoupStrainer
import re
from collections import defaultdict
import csv
import json
import time
import HTMLParser

# Unescape HTML Safe characts
h = HTMLParser.HTMLParser()

# Readability Website data
baseUrl = "https://readability.com/api/content/"
version = "v1"
apiType1 = "parser"
apiType2 = "confidence"
token = "0355da835a55164bb30c1f566a4a69b79b6e1b74"
rowCount = 0

# Open csv file containing good eats links
csvReadFile = open('goodEatsLinks.csv', 'rb')
goodEatsReader = csv.reader(csvReadFile, delimiter=',')

#Open csv file to store data from Readability
csvWriteFile = open('goodEatsData.csv', 'wb')
# fieldnames = ['season', 'title', 'content']
goodEatsWriter = csv.writer(csvWriteFile, delimiter=",")


for row in goodEatsReader:
	#parse article at URL
	getString = baseUrl + "/" + version + "/" + apiType1 + "?url=" + row[1] + "&token=" + token

	# Send request to readability.com
	response = requests.get(getString)
	# Parse Json Response to Python readable format
	parsed_response = json.loads(response.text)

	# print parsed_response['content']

	# Get and clean content from response
	transcriptContent = h.unescape(parsed_response["content"]).encode('utf-8')
	transcriptContent = re.sub('<[^>]*>', '', transcriptContent)
	transcriptContent = re.sub('[\xc2\xa0]+', '', transcriptContent)
	# transcriptContent = re.sub('[\\n]+', '', transcriptContent)
	transcriptContent = re.sub('[\s]+', ' ', transcriptContent)
	# transcriptContent = transcriptContent.encode('utf-8')


	#Get and clean title from response
	transcriptTitle = parsed_response["title"].encode('utf-8')
	transcriptTitle = re.sub(r'(?i)[\s]+Trancscript','',transcriptTitle)

	# Get season number
	transcriptSeason = row[0]

	#Write into csv file
	goodEatsWriter.writerow([transcriptSeason, transcriptTitle, transcriptContent])

	print "completed " + transcriptSeason + " : " + str(rowCount)
	rowCount += 1

	# so that I don't overstay my welcome with readability and to ensure most of the episodes are in order
	time.sleep(1)
	# break