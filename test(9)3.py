import xml.sax
import xml.sax.handler
from xml.sax.xmlreader import AttributesImpl

class MoviceHander( xml.sax.ContentHandler ):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if  tag == "movie":
            print("*****Movie*****")
            title = attributes["title"]
            print("Title: ", title)

    def endElement(self, tag):
        if self.CurrentData == "type":
            print("Type:", self.type)
        elif self.CurrentData == "format":
            print("Format:", self.format)
        elif self.CurrentData == "year":
            print("Year:", self.year)
        elif self.CurrentData == "rating":
            print("rating", self.rating)
        elif self.CurrentData == "stars":
            print("stars", self.stars)
        elif self.CurrentData == "description":
            print("description", self.description)
        self.description = ""
    
    def characters(self,content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content

if (__name__) == "__main__":

    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    
    Hander = MoviceHander()
    parser.setContentHandler( Hander )

    parser.parse("movie.xml")