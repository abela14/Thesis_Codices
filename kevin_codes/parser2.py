import random, os, time, re

global filename
KEYWORDS = ["write", "open", "read"]
CLASSES = ["spy","trojan","root","exploit"]

def openfile(filename):
	global file_p
	global filesize

	try:
		file_p = open("logs\\" + filename, 'r')
	except IOError:
		print "File not found."

def parsefile(parsefilename):
	data = file_p.readlines()
	file_w = open("parsedlogs\\" + parsefilename, 'w')
	for line in data:
		for word in KEYWORDS:
			if re.search(word, line):
				file_w.write(word + "\n")
	file_w.close

def closefile():
	file_p.close

def arfftranscriptor(mclass, parsedlog):
	try:
		file2_p = open("parsedlogs\\" + parsedlog, 'r')
	except IOError:
		print "File not found."
	
	data1 = file2_p.readlines()
	file2_w = open("sample_features.arff", 'a')
	
	counter = 0
	for word in KEYWORDS:
		for line in data1:
			if re.search(word, line):
				counter = counter + 1
		file2_w.write(str(counter) + ",")
	file2_w.write("'" + mclass + "'\n")
	file2_p.close
	file2_w.close

logs = os.listdir("logs")
for word in logs:
	openfile(word)
	parsefile("initialoutput.txt")
	for word2 in CLASSES:
		if re.search(word2,word):
			arfftranscriptor(word2,"initialoutput.txt")
	closefile()

