# coding:utf-8
import simplejson as json
import csv
from EpisodeClass import Episode

# File Data
filePath = ["../Data/", "../DataCleaned/"]
fileNameForReading = ["goodEatsMetadata.csv","goodEatsData.csv"]
fileNameForWriting = "episodeInformationOutput.json"

# File read and write pointers
metadataReader = csv.DictReader(open(filePath[0] + fileNameForReading[0], 'rb'), delimiter=",")
transcriptReader = open(filePath[0] + fileNameForReading[1], 'rb')
jsonWriter = open(filePath[1] + fileNameForWriting, 'wb')

# tempvar for debugging
count = 0
# Use @staticmethod getShowID as key for EpisodeList and TranscriptList Dictionaries
episodeList = {} 
transcriptList = {}

# MetaData operations
for line in metadataReader:
	print(line["b'Show #'"])
	# Create and store Metadata information for each episode
	# episode = Episode(line["b'Title'"])
	# episode.setEpisodeID(line["b'Show #'"])
	# episode.setEpisodeNumber(line["b'Show No.'"])
	# episode.addTopics(line["b'Topics'"])
	# episode.addRecipes(line["b'Recipes'"])
	# episode.addAirDate(line["b'Original Air Date'"])
	# episode.addTranscriptID(line["b'Transcript'"])

	# episodeList[Episode.getShowID(line[b'Show #'])] = episode

	count += 1

	if count > 3:
		break

# json.dump(episodeList, jsonWriter, sort_keys=True)





