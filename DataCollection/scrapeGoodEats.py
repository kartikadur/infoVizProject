# coding : utf-8
import csv
import requests
from bs4 import BeautifulSoup, SoupStrainer
import re


""" Update to python 3 and remove fileManager links and related code """
# Variables
urlList = list()
urlPart = list()
uri = list()
rowCount = 0

# Good Eats website data
websiteUrl = "http://www.goodeatsfanpage.com"
uri.append("gefp/episodebyorder.htm")

# regex matcher
regexPatterns = ['^\.\./Season\d+/[\w\-\_\.]+/[\w\-\_]+', '^\.\./Season\d+/\w+.htm[l]?$']
patterns = [re.compile(regexPatterns[0]), re.compile(regexPatterns[1])]

# file managers
filePath = "../Data/"
fileName = "goodEatsLinks.csv"

# response and request objects
response = requests.get("/".join([websiteUrl,uri[0]]))

# create and open file through file manager and store in file handler list
writeManager = csv.writer(open(filePath + fileName, 'w'), delimiter=",", lineterminator='\n')

# loop through all useful links
for link in BeautifulSoup(response.content, "html.parser", parse_only = SoupStrainer('a')):
	if(link.has_attr('href') and patterns[1].match(link['href'])):
		urlPart = link['href'].split('/', 2)
		urlPart.append(urlPart[2].split('.')[0])
	if(link.has_attr('href') and patterns[0].match(link['href'])):
		urlPart.append(link['href'].split('/', 2)[2])
		# unique episode id, season id, episode metadata url, episode transcript url
		writeManager.writerow([urlPart[3], 
								urlPart[1], 
								"/".join([websiteUrl,urlPart[1],urlPart[2]]), 
								"/".join([websiteUrl,urlPart[1],urlPart[4]])])

		print(urlPart[3], "Done!")
		# break