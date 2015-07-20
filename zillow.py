import xml.dom.minidom
import urllib2

api_key="ZILLOW API KEY" 
#This has to be the actual zillow API key for displaying the correct results.
#Modify the code for the key, otherwise only None will display.
#In order to run this correctly addresslist.txt must be in the same directory.

def address_data(address, city):
  adr = address.replace(' ', '+')
  url = 'http://www.zillow.com/webservice/GetDeepSearchResults.htm?'
  url += 'zws-id=%s&address=%s&citystatezip=%s' % (api_key, adr, city)
  doc = xml.dom.minidom.parseString(urllib2.urlopen(url).read())
  code = doc.getElementsByTagName('code')[0].firstChild.data
  if code != '0': 
    return None
  if 1:
    zipcode = doc.getElementsByTagName('zipcode')[0].firstChild.data
    usecodes = doc.getElementsByTagName('useCode')[0].firstChild.data
    year = doc.getElementsByTagName('yearBuilt')[0].firstChild.data
    squarefeet = doc.getElementsByTagName('finishedSqFt')[0].firstChild.data
    bathrooms = doc.getElementsByTagName('bathrooms')[0].firstChild.data
    bedrooms = doc.getElementsByTagName('bedrooms')[0].firstChild.data
    rooms = doc.getElementsByTagName('totalRooms')[0].firstChild.data
    price = doc.getElementsByTagName('amount')[0].firstChild.data
  else:
    return None
       
  return (zipcode, usecodes, int(year), int(bathrooms), int(bedrooms), int(rooms), price)

def pricelist():
  addresses = []
  for line in file('addresslist.txt'):
    data = address_data(line.strip(),'Redwood City, CA')
    addresses.append(data)
  return addresses

if __name__ == "__main__":
  print(pricelist())
