# This is a script to take the csv from google docs
# and turn it into just titles & artists so that I
# can fabricate search terms automatically

# The original CSV is included for reference

import sys
import json

filename = "music.csv"
data = ''
with open(filename, 'r') as file:
	data = file.readlines()


split = []
for song in data:
	song = song.split()
	song = ' '.join(song).split(',')
	split.append(song)

split = filter(None, split)

songjson = []
for song in split:
	details = {}
	details['title'] = song[1]
	details['artist'] = song[2]
	songjson.append(details)

#pprint(details)
del songjson[-1]
del songjson[0]

with open('output', 'w') as file:
	json.dump(songjson, file)
