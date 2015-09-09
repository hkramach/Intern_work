import xml.dom.minidom
import urllib2
import urllib
import json

def getAvailableDatasetJSON():
    response = urllib2.urlopen('http://www.bea.gov/api/data/?&UserID=F39EF1EC-4748-4EFB-B21A-E6A4A53E0449&method=GetData&DataSetName=GDPbyIndustry&Year=2010&Industry=11&tableID=ALL&Frequency=A,Q&ResultFormat=json')
    #api returns json
    return json.load(response)

def getAvailableDataset():
    url = 'http://www.bea.gov/api/data/?&UserID=F39EF1EC-4748-4EFB-B21A-E6A4A53E0449&method=GetData&DataSetName=GDPbyIndustry&Year=2010,2011,2012&Industry=11&tableID=ALL&Frequency=A,Q&ResultFormat=xml'
    #api returns xml
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    doc = xml.dom.minidom.parseString(response.read())
    return doc

if __name__ == "__main__":
  choice = raw_input("JSON or XML?")

  if choice == "XML":
    doc = getAvailableDataset()
    results = doc.getElementsByTagName('Results')
    #use xml to parse other fields example
    for i, elem in enumerate(results):
      print i, elem.nodeName
    print(doc.toxml())

  if choice == "JSON":
    print (getAvailableDatasetJSON())
