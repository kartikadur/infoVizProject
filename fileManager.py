# coding: utf-8
import csv

class fileManager:

	"""docstring for fileManager"""
	
	def __init__(self, fileName):
		self.fileName = fileName

	def openFile(self, openType = 'rb', delimiter = ','):
		self.filePointer = open(self.fileName, openType)
		if(openType == 'rb' or openType == 'r'):
			try:
				self.reader = csv.reader(self.filePointer, delimiter=delimiter)
			except Exception, e:
				raise e
		else :
			try:
				self.writer = csv.writer(self.filePointer, delimiter=delimiter)
			except Exception, e:
				raise e

	def closeFile(self):
		self.filePointer.close()

	def getRows(self):
		if(self.reader):
			return self.reader
		else:
			return None

	def writeRows(self, data = []):
		if(self.writer):
			self.writer.writerow(data)
		else:
			return None

if __name__ == '__main__':
	file1 = fileManager('goodEatsLinks.csv')
	file2 = fileManager('testEats.csv')
	file1.openFile()
	file2.openFile(openType='wb')
	for row in file1.getRows():
		file2.writeRows([row[1]])

	file1.closeFile()
	file2.closeFile()
	file2.openFile()
	for row in file2.getRows():
		print row
		