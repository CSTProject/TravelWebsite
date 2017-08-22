import dryscrape
from bs4 import BeautifulSoup

class Spider():
    def __init__(self, origin, destination, date, adults, childs, infants):
        url = 'https://www.cleartrip.com/flights/results?from=' + origin + '&to=' + destination + '&depart_date=' + date + '&adults=' + adults + '&childs=' + childs + '&infants=' + infants + '&sortType0=price&sortOrder0=sortAsc&page=loaded'
        try:
            dryscrape.start_xvfb()
            session = dryscrape.Session()
            session.visit(url)
            response = session.body()
            self.source = response
            print("GOT DATA,STARTING SCRAPING\n\n")
            print(response + "\n\n")
        except:
            print("WARNING : CHECK INTERNET CONNECTION, CAN'T GET DATA FROM THE INTERNET")
            self.source = ''

    def GetLength(self):
        soup = BeautifulSoup(self.source, "lxml")
        data = []
        for table in soup.findAll('th', {'id': 'BaggageBundlingTemplate'}):
            data.append(table.text)
        return len(data)

    def FixData(self, fixthis, length):
        for i in range(0,length):
            fixthis[i] = fixthis[i].replace("\n","")
            fixthis[i] = " ".join(fixthis[i].split())
            fixthis[i] = fixthis[i].strip()
        return fixthis


    def GetPrices(self):
        soup = BeautifulSoup(self.source, "lxml")
        data = []
        for table in soup.findAll('th', {'id': 'BaggageBundlingTemplate'}):
            data.append(table.text )
        return self.FixData(data,self.GetLength())

    def GetDepartureTime(self):
        soup = BeautifulSoup(self.source, "lxml")
        data = []
        for table in soup.findAll('th', {'class':'depart'}):
            data.append(table.text)
        return self.FixData(data,self.GetLength())
    def GetArrivalTime(self):
        soup = BeautifulSoup(self.source, "lxml")
        data = []
        for table in soup.findAll('th', {'class':'arrive'}):
            data.append(table.text)
        return self.FixData(data,self.GetLength())
    def GetDurationTime(self):
        soup = BeautifulSoup(self.source, "lxml")
        data = []
        for table in soup.findAll('th', {'class':'duration'}):
            data.append(table.text)
        return self.FixData(data,self.GetLength())
    def GetStops(self):
        soup = BeautifulSoup(self.source, "lxml")
        data = []
        for table in soup.findAll('td', {'class':'duration'}):
            data.append(table.text)
        return self.FixData(data,self.GetLength())
    def GetRoute(self):
        soup = BeautifulSoup(self.source, "lxml")
        data = []
        for table in soup.findAll('td', {'class':'route'}):
            data.append(table.text)
        return self.FixData(data,self.GetLength())
    def GetVendor(self):
        soup = BeautifulSoup(self.source, "lxml")
        data = []
        for table in soup.findAll(['th','td'], {'class':['vendor','vendor  count1']}):
            if (table.text != ''):
                data.append(table.text)
            else:
                for image in soup.findAll("img"):
                    try:
                        data.append(image.get('alt', ''))
                    except:
                        data.append(table.text)

        return self.FixData(data,self.GetLength())
    def GetDictionary(self):
        dict = {'Serial':[],'Prices':[],'DepartTime':[],'Time':[],'Stops':[],'ArrivalTime':[],'Route':[],'Vendor':[]}
        list1 = self.GetPrices()
        list2 = self.GetDepartureTime()
        list3 = self.GetDurationTime()
        list4 = self.GetStops()
        list5 = self.GetArrivalTime()
        list6 = self.GetRoute()
        list7 = self.GetVendor()
        for position in range(0,self.GetLength()):
            dict['Serial'].append(str(position))
            dict['Prices'].append(list1[position])
            dict['DepartTime'].append(list2[position])
            dict['Time'].append(list3[position])
            dict['Stops'].append(list4[position])
            dict['ArrivalTime'].append(list5[position])
            dict['Route'].append(list6[position])
            dict['Vendor'].append(list7[position])

        return dict




'''CODE BELOW ONLY FOR DEBUGGING AND TESTING
print("Enter Start Location")
start = input()
print("Enter Stop Location")
end = input()
print("Enter Date in format dd/mm/yyyy")
date = input()
print("Enter Adults")
adults = input()
print("Enter Childs")
child = input()
print("Enter Infants")
infant = input()
print("Processing...")
spiders = Spider(start,end,date,adults,child,infant)



list1 = spiders.GetPrices()
list2 = spiders.GetDepartureTime()
list3 = spiders.GetDurationTime()
list4 = spiders.GetStops()
list5 = spiders.GetArrivalTime()
list6 = spiders.GetRoute()
list7 = spiders.GetVendor()
for i in range(0,spiders.GetLength()):
    print(str(i+1) + '.\nPrice: ' + list1[i])
    print('Vendor: ' + list7[i])
    print('Departure Time: ' + list2[i])
    print('Arrival Time: ' + list5[i])
    print('Duration: ' + list3[i])
    print('Number of Stops: ' + list4[i])
    print('Route: ' + list6[i])

print(spiders.GetDictionary())


'''