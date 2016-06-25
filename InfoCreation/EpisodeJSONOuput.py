# coding:utf-8
import simplejson as json
import csv
from EpisodeClass import Episode
from collections import OrderedDict

# File Data
filePath = ["../Data/", "../DataCleaned/"]
fileNameForReading = ["goodEatsMetadata.csv","goodEatsData.csv"]
fileNameForJSON = "episodeInformationOutput.json"
fileNameForCSV = "csvOutput.csv"

fieldnames = ['showTitle', 'episodeID',  'episodeNumber', 'seasonNumber', 'seasonEpisodeNumber', 'airDate']

# File read and write pointers
metadataReader = csv.DictReader(open(filePath[0] + fileNameForReading[0], 'r', encoding='utf-8'), delimiter=',')
transcriptReader = csv.reader(open(filePath[0] + fileNameForReading[1], 'r', encoding='utf-8'), delimiter=',')
jsonWriter = open(filePath[1] + fileNameForJSON, 'w', encoding='utf-8')
fileNameForCSV = "csvOutput.csv"
csvWriter = csv.DictWriter(open(filePath[1] + fileNameForCSV, 'w', encoding='utf-8'), delimiter=',', lineterminator='\n', fieldnames=fieldnames)

# tempvar for debugging
count = 0
# Use @staticmethod getShowID as key for EpisodeList and TranscriptList Dictionaries
# episodeList = OrderedDict() 
# transcriptList = {}


""" MetaData operations for force graph"""
# for line in metadataReader:
# rNodesList, nodesList = [],[]
# linksList = []

# 	rNodesList.append({'name': Episode.getShowID(line['Show #']), 'group' : Episode.getSeasonNumber(line['Show #'])})

# nodesListLength = len(rNodesList)
# for i in range(0, nodesListLength):
# 	nodesList.append(rNodesList[nodesListLength - i - 1])
# 	if i > 0:
# 		linksList.append({'source' : i - 1, 'target' : i, 'value' : 1})

# json.dump({ 'nodes' : nodesList, 'links' : linksList}, jsonWriter)

""" CSV Data-Subset for visualization """
dataset = {}

csvWriter.writeheader()

for line in metadataReader:
	episode = Episode(line['Title'])
	episode.setEpisodeID(line['Show #'])
	episode.setEpisodeNumber(line['Show No.'])
	episode.addAirDate(line['Original Air Date'])
	csvWriter.writerow(episode.__dict__)




