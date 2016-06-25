import simplejson as json
import csv
from EpisodeClass import Episode
from collections import OrderedDict, defaultdict

filePath = ['../Data', '../DataCleaned']
readFiles = ['goodEatsMetadata.csv', 'goodEatsData.csv']
writeFiles = ['goodEatsJSONData.json']

metadataReader = csv.DictReader(open('/'.join([filePath[0], readFiles[0]]), 'r', encoding='utf-8'), delimiter=',')
dataReader = csv.reader(open('/'.join([filePath[0], readFiles[1]]), 'r', encoding='utf-8'), delimiter=',')
jsonWriter = open('/'.join([filePath[1], writeFiles[0]]), 'w', encoding='utf-8')

# tempvars for debugging and short termination of loops
count = 0
episodeList = defaultdict(list)

for line in metadataReader:
	episode = Episode(line['Title'])
	episode.setEpisodeID(line['Show #'])
	episode.setEpisodeNumber(line['Show No.'])
	episode.addAirDate(line['Original Air Date'])
	episode.addTopics(line['Topics'])
	episode.addRecipes(line['Recipes'])
	episode.addTranscriptID(line['Transcript'])
	if episode.getSeasonNumber(line['Show #']) in episodeList:
		episodeList[episode.getSeasonNumber(line['Show #'])].append(episode.__dict__)
	else :
		episodeList[episode.getSeasonNumber(line['Show #'])] = [episode.__dict__]

json.dump(episodeList, jsonWriter)
