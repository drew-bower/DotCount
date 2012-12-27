#!/usr/bin/env python
	 
import sys

cnt = 0

scaleFactor = 1.0/3600.0
	 
# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split the line into words
	field = line.split(',')
	# print field
	lat = float(field[2].strip())
	lon = float(field[3].strip())
	# print lat, lon
	latHash = (int((lat - float(int(lat))) / scaleFactor) * scaleFactor) + float(int(lat))
	lonHash = (int((lon - float(int(lon))) / scaleFactor) * scaleFactor) + float(int(lon))
	print "%s,%s\t1" % (latHash, lonHash)
# print cnt
