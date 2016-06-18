# coding:utf-8
import simplejson as json
import csv
from EpisodeClass import Episode

# File Data
filePath = "../DataCleaned/"
fileNameForReading = ["GoodEatsMetadata.csv - goodEatsMetadata.csv","GoodEatsTranscriptData.csv - goodEatsData.csv"]
fileNameForWriting = "episodeInformationOutput.json"

# File read and write pointers
metadataReader = csv.DictReader(open(filePath + fileNameForReading[0], 'r'), delimiter=",")
transcriptReader = open(filePath + fileNameForReading[1], 'r')
jsonWriter = open(filePath + fileNameForWriting, 'w')

# count = 0
episodeList = [] # Needs a new data structure that will store the show ID specifically as the key
transcriptList = {}

# DataContent Operations
for line in transcriptReader:
	print(line[150:202])

# # MetaData operations
# for line in metadataReader:
	
# 	episode = Episode(line['Title'])
# 	episode.setEpisodeID(line['Show #'])
# 	episode.setEpisodeNumber(line['Show No.'])
# 	episode.addTopics(line['Topics'])
# 	episode.addRecipes(line['Recipes'])
# 	episode.addAirDate(line['Original Air Date'])
# 	episode.addTranscriptID(line['Transcript'])

# 	episodeList.append(episode.__dict__)

# 	# print(json.dumps(episode.__dict__))

	
# 	# count += 1

# 	# if count > 3:
# 	# 	break

# json.dump(episodeList, jsonWriter, sort_keys=True)





