import pprint as p
import etlParser as parser


fileName = "Eng2Rus.json"
word = 'help'

# obj = JSONParser('Eng2Rus.json')
# index = obj.genIndex()
# pos = obj.findPosition("find", index)
# rec = obj.getRecord(pos)
# print(rec)


jp = parser.JSONParser(fileName)
index = jp.genIndex()
wordPos = jp.findPosition(word, index)
rec = jp.getRecord(wordPos)

p.pprint(rec)


# # Isolate Each word in description
# tmpArr = []
# word = ''
# for d in rec['description']:
# 	for i in d:
# 		word += i
# 		if i == " " or i == '\n' and len(i) > 1:
# 			tmpArr.append(word)
# 			print(word)
# 			word = ""
# count = 0
# newArr = []
# for i in tmpArr:
# 	if i != " ":
# 		newArr.append(i)

# for i in newArr:
# 	count += 1
# 	#print(count, ": ",i)




