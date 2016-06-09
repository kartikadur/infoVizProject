import csv
from EpisodeClass import Episode
import json


filePath = "../DataCleaned/"
fileName = "GoodEatsMetadata.csv - goodEatsMetadata.csv"
fileName2 = "GoodEatsTranscriptData.csv - goodEatsData.csv"

filePointer = open(filePath + fileName, "rb")
fileReader = csv.DictReader(filePointer, delimiter=",")
episodeList = {}
episodeTranscriptList = {}

filePointer2 = open(filePath + fileName2, "rb")
fileReader2 = csv.reader(filePointer2, delimiter=",")


for rows in fileReader2:
	episodeTranscriptList[rows[0]] = rows[3]


for rows in fileReader:
	ep = Episode(rows['Title'])
	ep.setShowID(rows["Show #"])
	ep.setShowNumber(rows["Show No."])
	ep.addTopics(rows["Topics"])
	ep.addAirDate(rows["Original Air Date"])
	ep.addRecipes(rows["Recipes"])
	ep.addTranscriptID(rows["Transcript"])
	if rows["Show #"] in episodeTranscriptList:
		ep.addTranscript(episodeTranscriptList[rows["Show #"]])
	# print json.dumps(ep.__dict__)
	episodeList[ep.showID] = ep



# This is how the json output should look
# count = 0
# data = "["
# for episode in episodeList:
# 	if count >= 1:
# 		data += ","
# 	data += json.dumps(episodeList[episode].__dict__)

# 	count += 1
# 	if count >= 4:
# 		break
# data += "]"

# print data