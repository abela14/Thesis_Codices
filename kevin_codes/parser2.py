import random, os, time, re

global filename
KEYWORDS = ["write", "open", "read"]

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
		for word in KEYWORDS:
			if re.search(word, line):
				file_w.write(word + "\n")
	file_w.close

def closefile():
	file_p.close

def arfftranscriptor():
	try:
		file2_p = open("sample_parsed.txt", 'r')
	except IOError:
		print "File not found."
	
	data1 = file2_p.readlines()
	file2_w = open("sample_features.arff", 'w')
	
	file2_w.write("%SAMPLE ARFF FOR APPLICATION FEATURE \n@relation 'features' \n@attribute 'write' numeric \n@attribute 'read' numeric \n@attribute 'open' numeric \n@attribute 'class' {'trojan', 'virus'} \n\n@data \n")
	counter = 0
	for word in KEYWORDS:
		for line in data1:
			if re.search(word, line):
				counter = counter + 1
		file2_w.write(str(counter) + ",")
	file2_w.write("'DogOWar'\n")
	file2_p.close
	file2_w.close

	
openfile("DogOWar2.txt")
readfile()
closefile()
arfftranscriptor()

