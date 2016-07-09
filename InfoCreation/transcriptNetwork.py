# coding:utf-8
import csv
import simplejson as json
from EpisodeClass import Episode
from collections import OrderedDict


filePath = ['../Data','../DataCleaned']
inputFileName = ['goodEatsMetadata.csv', 'goodEatsData.csv']
outputFileName = ['testNetwork.json']


# File Handlers / File Pointers
readMetadata = csv.DictReader(open('/'.join([filePath[0], inputFileName[0]]), 'r'), delimiter=',')
readData = csv.reader(open('/'.join([filePath[0], inputFileName[1]]), 'r', encoding='utf-8'), delimiter=',')
writeData = open('/'.join([filePath[1], outputFileName[0]]), 'w', encoding='utf-8')

# Data Structure to hold network node and connectivity information
nodesList, linksList, nodeIDs = [],[],[]
episodeList, jsonEpisodeList = {},{}

# Create Episode instances and store into dict using showID
for line in readMetadata:
	episode = Episode(line['Title'])
	episode.setEpisodeID(line['Show #'])
	episode.addTranscriptID(line['Transcript'])
	# print(episode.__dict__)
	episodeList[Episode.getShowID(line['Show #'])] = episode
	nodeIDs.append(Episode.getShowID(line['Show #']))
	# break

# Add 'another show' as an extra show as it is always referenced
# in the show but never really links anywhere, so put it as a dead-end link
episode = Episode('Referenced Mystery Show')
episode.setEpisodeID('EA0000')
episode.addTranscriptID('Another Show')
episodeList[Episode.getShowID('EA0000')] = episode
nodeIDs.append(Episode.getShowID('EA0000'))
print(nodeIDs)

# Add transcript to each episode instance
for data in readData:
	episodeList[Episode.getShowID(data[0])].addTranscript(data[1])


for ep in episodeList:
	jsonEpisodeList[ep] = episodeList[ep].__dict__

# nodeIDs = sorted(nodeIDs)

# loop i from 1 to n-1 and j from i+1 to n
for i in nodeIDs:
	for j in nodeIDs:
		if i < j and len(jsonEpisodeList[i]['transcriptID'].lower()) > 2 and jsonEpisodeList[i]['transcriptID'].lower() in jsonEpisodeList[j]['transcriptContent'].lower() :
			linksList.append({
				'source': i,
				'target': j,
				'value': 1
				})
			nodesList.append({
				'id': i,
				'name': jsonEpisodeList[i]['showTitle'],
				'group': jsonEpisodeList[i]['seasonNumber']
				})
			nodesList.append({
				'id': j,
				'name': jsonEpisodeList[j]['showTitle'],
				'group': jsonEpisodeList[j]['seasonNumber']
				})

json.dump({'links': linksList, 'nodes':list({v['id']: v for v in nodesList}.values())}, writeData)