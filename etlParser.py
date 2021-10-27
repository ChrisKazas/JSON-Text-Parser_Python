'''     Python 3.7.4
	Author: Chris Kazas
	8-14-2019

	Python Module to parse through JSON file as part of etl pipeline

	findPosition  -> int
	   Opens file at position provided by genIndex method
	   Parses through file looking for position of record
	   returning the position of specific record as integer

	genIndex      -> dict
	   Opens file and generates a dict where the key(str) = letter of
 	   alphabet and value(int) = position of curser in file of first
	   instance of of each letter of alphabet

	getRecord     -> dict
	   Opens file at position generated from findPosition method, parses
	   through file looking for end of record stripping out unnecessary
	   white space and chars  creating dict containing Rnglish version of
	   word, array of Russian descriptions of English word, size of array
	   Russian descriptions

	isMatch       -> boolean
	   Takes in array of strs and a str and searches array for instance
	   of str returning boolean
'''

import json as json
import codecs as codecs


class JSONParser():

	def __init__(self,fileName):
		self.fileName = fileName

	# Parse file generating dict containing file position
	# of first instance of first letter of word
	def genIndex(self):

		delimeter = '","'
		prev = ''
		curr = 'a'
		index = {}
		try:
			with open(self.fileName, 'r+b') as f:
				for line in f:
					rawData = codecs.decode(f.readline())
					if rawData[0:3] == delimeter:
						curr = rawData[3:4]
					if curr != prev:
						index[curr] = f.tell()
						prev = curr
						if curr == 'z':
							break
			return index

		except Exception as e:
			print("ERROR: ", e)


	#
	def findPosition(self, word, index):

		# Generate file index by first letter
		# of each word and position in file
		#index = genIndex(self.fileName)

		# Get index on end next letter in dict
		i = iter(index)
		while True:
			if next(i) == word[0]:
				break

		# start and end position for file search
		startPos = index[word[0]]
		endPos = index[next(i)]

		# Open file at position indexed by fist letter
		# search file returning position of word in file
		# or -1 if word != exist
		try:
			with open(self.fileName, 'r+b') as f:
				f.seek(startPos)
				while f.tell() != endPos:
					rawData = codecs.decode(f.readline())
					wrdSrch = '","'+ word + '":"'
					if rawData[0:len(wrdSrch)] == wrdSrch:
						return f.tell()
					if f.tell() == endPos:
						print("{} not found!!".format(word))
						return -1

		except Exception as e:
			print("ERROR:", e)


	#
	def getRecord(self, filePosition):

		try:
			with open(self.fileName,'r+b') as f:
				# open file at postion by filePosition arg
				f.seek(filePosition)
				record =''
				delimeter= '","'

				# build record str until delimiter reached
				while delimeter not in record:
					record += codecs.decode(f.readline())

				# Isolate record
				x = record.find('","')
				record = record[0:x]

				# Isolate english word
				x = record.find(" ")
				engWord = record[0:x-1]

				# Isolate description
				desc = record[x:]

				# Strip wite space and numbers from dscrptn
				desc = desc.splitlines()
				desc = desc[1:]
				descArr = []
				tmpWrd = ''
				for i in desc:
					i.rstrip()
					delIndx = i.find(':')
					tmpWrd = i[delIndx+2:]
					if tmpWrd[0] != ' ':
						descArr.append(tmpWrd)


				# Populate record object
				recObj ={}
				recObj['engWord'] = engWord
				recObj['description'] = descArr
				recObj['size'] = len(descArr)

				return recObj
				# Unit Testing
				#p.pprint(recObj)

		except Exception as e:
			print("ERROR: ", e)

	#
	def isMatch(arr, word):

		if len(arr) < 1:
			print("ERROR: arg1 is an empty array")
			return

		# Itr through arr of strs looking for sub str
		for i in arr:
			if word in i:
				return True
			else:
				return False






# # Unit Testing
# obj = JSONParser('Eng2Rus.json')
# index = obj.genIndex()
# pos = obj.findPosition("find", index)
# rec = obj.getRecord(pos)
# print(rec)





