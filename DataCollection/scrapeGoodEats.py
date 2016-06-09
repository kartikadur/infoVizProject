from fileManager import fileManager
import csv
import requests
from bs4 import BeautifulSoup, SoupStrainer
import re

# Variables
urlList = list()
urlPart = list()
uri = list()
rowCount = 0

# Good Eats website data
websiteUrl = "http://www.goodeatsfanpage.com/"
uri.append("gefp/episodebyorder.htm")

# regex matcher
regexPatterns = ['^\.\./Season\d+/\w+/\w+', '^\.\./Season\d+/\w+.htm[l]?$']
patterns = [re.compile(regexPatterns[0]), re.compile(regexPatterns[1])]

# file managers
fileNames = ['goodEatsLinks.csv']
fileHandler = list()

# response and request objects
response = requests.get(websiteUrl + uri[0])

# create and open file through file manager and store in file handler list
fileHandler.append(fileManager(fileNames[0]))
fileHandler[0].openFile('wb')


# loop through all useful links
for link in BeautifulSoup(response.content, "html.parser", parse_only = SoupStrainer('a')):
	if(link.has_attr('href') and patterns[1].match(link['href'])):
		urlPart = link['href'].split('/', 2)
		urlPart.append(urlPart[2].split('.')[0])
	if(link.has_attr('href') and patterns[0].match(link['href'])):
		urlPart.append(link['href'].split('/', 2)[2])
		# unique episode id, season id, episode metadata url, episode transcript url
		fileHandler[0].writeRows([urlPart[3], 
									urlPart[1], 
									websiteUrl + urlPart[1] + '/' + urlPart[2], 
									websiteUrl + urlPart[1] + '/' + urlPart[4]])

# close file handler
fileHandler[0].closeFile();