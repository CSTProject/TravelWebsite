import requests

class RailwatApi():
    def __init__(self,train_no,date):
        self.train_no = str(train_no)
        self.date = str(date)

    def getJson(self):
         req = requests.get('http://api.railwayapi.com/v2/live/train/{}/date/{}/apikey/m6fb4klhgh/'.format(self.train_no,self.date))
         data = req.json()
         return data
    def stationlist(self):
        data = self.getJson()
        stationlist = []
        for i in range(0,len(data['route'])):
             stationlist.append(data['route'][i]['station']['name'])
        return stationlist




api = RailwatApi('12012','17-08-2017')
l = api.stationlist()
print(l)



