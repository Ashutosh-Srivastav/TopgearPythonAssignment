'''Question
8. Create a suitable data construct to read the data from an xml document as shown below:
<bookstore shelf="New Arrivals">
  <book category="COOKING">
    <title lang="en">Everyday Italian</title>
    <author>Giada De Laurentiis</author>
    <year>2005</year>
    <price>30.00</price>
  </book>
  <book category="CHILDREN">
    <title lang="en">Harry Potter</title>
    <author>J K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
  </book>
  <book category="WEB">
    <title lang="en">Learning XML</title>
    <author>Erik T. Ray</author>
    <year>2003</year>
    <price>39.95</price>
  </book>
</bookstore>
Question'''
#program
import xml.sax

class BookHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.title = ""
      self.author = ""
      self.year = ""
      self.price = ""
      #self.stars = ""
      #self.description = ""

   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "book":
         print "*****book*****"
         category = attributes["category"]
         print "category:", category

   # Call when an elements ends
   def endElement(self, tag):
      if self.CurrentData == "title":
         print "Title:", self.title
      elif self.CurrentData == "author":
         print "Author:", self.author
      elif self.CurrentData == "year":
         print "Year:", self.year
      elif self.CurrentData == "price":
         print "Price:", self.price
      #elif self.CurrentData == "stars":
        # print "Stars:", self.stars
      #elif self.CurrentData == "description":
        # print "Description:", self.description
      self.CurrentData = ""

   # Call when a character is read
   def characters(self, content):
      if self.CurrentData == "title":
         self.title = content
      elif self.CurrentData == "author":
         self.author = content
      elif self.CurrentData == "year":
         self.year = content
      elif self.CurrentData == "price":
         self.price = content
      #elif self.CurrentData == "stars":
        # self.stars = content
      #elif self.CurrentData == "description":
        # self.description = content

if ( __name__ == "__main__"):

   # create an XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = BookHandler()
   parser.setContentHandler( Handler )

   parser.parse("book.xml")


'''Solution
osgdev@DHZ-PES13:~/pythonas338011/PythonL1Assignment$ python 8.py
*****book*****
category: COOKING
Title: Everyday Italian
Author: Giada De Laurentiis
Year: 2005
Price: 30.00
*****book*****
category: CHILDREN
Title: Harry Potter
Author: J K. Rowling
Year: 2005
Price: 29.99
*****book*****
category: WEB
Title: Learning XML
Author: Erik T. Ray
Year: 2003
Price: 39.95
Solution'''
