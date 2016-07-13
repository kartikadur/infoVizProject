# encoding : utf-8
import csv
import re
from dataManager import DataCollector, DataCleaner

# File Handling
filePath = ['../Data', '../DataCleaned']
fileName = ['futurama_links.csv', 'futurama_transcripts.csv']

fileReader = csv.reader(open('/'.join([filePath[0], fileName[0]]), 'r', encoding='utf-8'), delimiter=',')
fileWriter = csv.writer(open('/'.join([filePath[1], fileName[1]]), 'w', encoding='utf-8'), delimiter=',', lineterminator='\n')

# data manager
dcol = DataCollector()
dcls = DataCleaner()

for line in fileReader:
	content = dcol.MakeHTTPRequest(line[3])

	# strip tags
	content = re.sub('<[^>]*>', '', content)

	content = dcls.ConvertHTMLToUnicode(content)
	content = dcls.CleanDataUsingRegex(r'(&#160;)+', ' ', content)
	content = dcls.CleanDataUsingRegex(r'[\r\n]', '', content)
	content = dcls.CleanDataUsingRegex(r'[\s]+', ' ', content)
	content = dcls.CleanDataUsingRegex(r'[’]', '\'', content)
	

	fileWriter.writerow([line[0], line[1], content])

	print('Completed transcript for episode {}'.format(line[1]))

	# single iteration debug
	# break
