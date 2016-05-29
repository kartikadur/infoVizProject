from fileManager import fileManager
import csv
import requests
from bs4 import BeautifulSoup, SoupStrainer
import re
# from collections import defaultdict


# # Create Vars
# urlList = defaultdict(list);
# uri = list()

# # create regular expression to check with
# # check that the url matches the pattern '../Season[xx]/some_name_here/page_name_here.htm'
# pattern = re.compile("^\.\./Season\d+/\w+/\w+")

# # Good Eats website data
# websiteUrl = "http://www.goodeatsfanpage.com/"
# uri.append("gefp/episodebyorder.htm");

# # Send request to website
# response = requests.get(websiteUrl + uri[0])


# #Open CSV file to write URLs
# with open('goodEatsLinks.csv', 'wb') as csvFile:
# 	goodEatsWriter = csv.writer(csvFile, delimiter=',')
# 	# Iterate through links on page
# 	# Store links in dictionary indexed by season
# 	for link in BeautifulSoup(response.content, "html.parser", parse_only = SoupStrainer('a')):
# 		if(link.has_attr('href') and pattern.match(link['href'])):
# 			# replace relative urls with absolute urls and store in data var
# 			urlParts = link['href'].split('/',2)
# 			# urlList[urlParts[1]].append(websiteUrl + urlParts[1] + '/' + urlParts[2])
# 			goodEatsWriter.writerow([urlParts[1], websiteUrl + urlParts[1] + '/' + urlParts[2]])


# Variables
# goodEatsData = defaultdict(list)
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


for link in BeautifulSoup(response.content, "html.parser", parse_only = SoupStrainer('a')):
	if(link.has_attr('href') and patterns[1].match(link['href'])):
		urlPart = link['href'].split('/', 2)
	if(link.has_attr('href') and patterns[0].match(link['href'])):
		urlPart.append(link['href'].split('/', 2)[2])
		fileHandler[0].writeRows([urlPart[1], websiteUrl + urlPart[1] + '/' + urlPart[2], websiteUrl + urlPart[1] + '/' + urlPart[3]])

fileHandler[0].closeFile();
