import csv
from EpisodeClass import Episode
import json


filePath = "../DataCleaned/"
fileName = "GoodEatsMetadata.csv - goodEatsMetadata.csv"

filePointer = open(filePath + fileName, "rb")
fileReader = csv.DictReader(filePointer, delimiter=",")
episodeList = []

for rows in fileReader:
	ep = Episode(rows["Show #"], rows['Title'])
	ep.setShowNumber(rows["Show No."])
	ep.addTopics(rows["Topics"])
	ep.addAirDate(rows["Original Air Date"])
	ep.addRecipes(rows["Recipes"])
	ep.addTranscriptID(rows["Transcript"])
	print json.dumps(ep.__dict__)
	episodeList.append(ep)
