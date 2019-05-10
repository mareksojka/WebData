import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = 'http://python-data.dr-chuck.net/comments_372119.xml'
	#raw_input('Enter location: ')
    if len(address) < 1 : break

    #url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
    url=address
	print ('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print ('Retrieved',len(data),'characters')
    print (data)
    tree = ET.fromstring(data)

	counts = tree.findall('.//count')
	coutnsum=0
	for count in counts:
		countsum+=int(count.text)
		
	
	
    #results = tree.findall('result')
    #lat = results[0].find('geometry').find('location').find('lat').text
    #lng = results[0].find('geometry').find('location').find('lng').text
    #location = results[0].find('formatted_address').text

    #print ('lat',lat,'lng',lng)
    #print (location)
