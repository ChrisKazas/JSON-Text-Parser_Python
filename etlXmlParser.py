import codecs as codecs
import unicodedata as ucd
import bytes

data = ''
eof = 0
cur_pos = 0
rawData =''
'Kто попало'.decode('utf-8', ignore)

try:
	with codecs.open("Rus2Eng.xml", 'r+b', 'utf-8') as f:
		for line in f:
			if line.find(wordSrch):
				print(f.tell())

except Exception as e:
	print("ERROR: ", e)



str1 = 'abcdefg'
str2 = 'c'

if str1.find(str2):
	print(str1.find(str2))
else:
	print('Not Found')
