import xml.sax as xml


class XMLHandler(xml.handler.ContentHandler):

	def __init__(self):
		self.currdata = ""
		self.engWord = ""
		self.rusWord = ""

	def startElement(self, startTag):
		pass

	def endElement(self, endTag):
		if endTag == "ar":
			print(self.currData)

	def characters(self, content):
		if content == 'ar':
			self.currData = content



if __name__ == '__main__':

	parser = xml.make_parser()
	parser.feed("Rus2Eng.xml")

	hndl = XMLHandler()
        parser.parse(hndl)



