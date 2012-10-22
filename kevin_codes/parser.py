import random, os, time, re

global filename
KEYWORDS = ['write']

def openfile(filename):
	global file_p
	global filesize

	try:
		file_p = open(filename, 'r')
		filesize = os.path.getsize(filename)
	except IOError:
		print "File not found."

def readfile():
	data = file_p.readlines()
	file_w = open("sample_parsed.txt", 'w')
	for line in data:
		for word in line.split():
			if word in KEYWORDS:
				file_w.write(line)

def closefile():
	file_p.close

openfile("DogOWar2.txt")
readfile()
closefile()

