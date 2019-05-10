import urllib.request
import json

url=input('Enter location: ')
jsonread=urllib.request.urlopen(url)
jsonfile=jsonread.read().decode("utf-8")
jsondata=json.loads(jsonfile)
print(json.dumps(jsondata,indent=4)

countsum=0
for item in jsondata['comments']:
    print ('Name', item['name'],' count', item['count'])
    countsum+=int(item['count'])
	
print(countsum)

