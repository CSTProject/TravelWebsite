import requests

r = requests.get('http://api.railwayapi.com/v2/live/train/12012/date/17-08-2017/apikey/m6fb4klhgh/')
p = r.json()
print(p)
print("************************")
print(p['route'][0]['schdep'])

'''
import urllib.request
import urllib.parse


url = 'http://api.railwayapi.com/v2/live/train/12012/date/17-08-2017/apikey/m6fb4klhgh/'
f = urllib.request.urlopen(url)
print(f.read().decode('utf-8'))

'''

'''
import urllib.request,json

with urllib.request.urlopen("http://api.railwayapi.com/v2/live/train/12012/date/17-08-2017/apikey/m6fb4klhgh/") as url:
    data = json.loads(url.read().decode())
    print(data)
'''
