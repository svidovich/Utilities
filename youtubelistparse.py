import json
import sys
from pprint import pprint

filename = 'weddinglist'
data = []
with open(filename, 'r') as file:
	data = json.load(file)


for entry in data:
	link = entry['link']
	link = 'https://www.youtube.com{}'.format(link)
	with open('outfile', 'a') as file:
		file.write('{}\n'.format(link))


