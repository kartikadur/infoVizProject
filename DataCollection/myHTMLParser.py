# coding: utf-8
from bs4 import BeautifulSoup
import re
import json

"""Good eats episode metadata"""

soup = BeautifulSoup(testData, "html.parser")
table = soup.find_all("table")[-1:]

datasets = []

for row in table[0].find_all("tr"):
	dataset = []
	for td in row.find_all("td"): dataset.append(td.get_text())
	datasets.append(dataset)
	# break

print datasets