# coding:utf-8
import simplejson as json
import csv
from EpisodeClass import Episode
from collections import OrderedDict

# File Data
filePath = ["../Data/", "../DataCleaned/"]
fileNameForReading = ["goodEatsMetadata.csv","goodEatsData.csv"]
fileNameForWriting = "episodeInformationOutput.json"

# File read and write pointers
metadataReader = csv.DictReader(open(filePath[0] + fileNameForReading[0], 'r', encoding='utf-8'), delimiter=',')
transcriptReader = csv.reader(open(filePath[0] + fileNameForReading[1], 'r', encoding='utf-8'), delimiter=',')
jsonWriter = open(filePath[1] + fileNameForWriting, 'w', encoding='utf-8')

# tempvar for debugging
count = 0
# Use @staticmethod getShowID as key for EpisodeList and TranscriptList Dictionaries
# episodeList = OrderedDict() 
# transcriptList = {}

rNodesList, nodesList = [],[]
linksList = []

# MetaData operations
for line in metadataReader:

	rNodesList.append({'name': Episode.getShowID(line['Show #']), 'group' : Episode.getSeasonNumber(line['Show #'])})

nodesListLength = len(rNodesList)
for i in range(0, nodesListLength):
	nodesList.append(rNodesList[nodesListLength - i - 1])
	if i > 0:
		linksList.append({'source' : i - 1, 'target' : i, 'value' : 1})

json.dump({ 'nodes' : nodesList, 'links' : linksList}, jsonWriter)

# 	# Create and store Metadata information for each episode
# 	episode = Episode(line['Title'])
# 	episode.setEpisodeID(line['Show #'])
# 	episode.setEpisodeNumber(line['Show No.'])
# 	episode.addTopics(line['Topics'])
# 	episode.addRecipes(line['Recipes'])
# 	episode.addAirDate(line['Original Air Date'])
# 	episode.addTranscriptID(line['Transcript'])

# 	episodeList[Episode.getShowID(line['Show #'])] = episode

# 	# print(episode.__dict__)

# 	count += 1

# 	if count > 3:
# 		break

# properOrderEpisodeList = OrderedDict(sorted(episodeList.items()))
# for ep in properOrderEpisodeList:
# 	print(ep, properOrderEpisodeList[ep].__dict__)
# # json.dump(episodeList, jsonWriter, sort_keys=True)





