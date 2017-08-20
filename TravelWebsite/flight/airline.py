import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage
from bs4 import BeautifulSoup

class Client(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.app.quit()

class Spider():
    def __init__(self, origin, destination, date, adults, childs, infants):
        url = 'https://www.cleartrip.com/flights/results?from=' + origin + '&to=' + destination + '&depart_date=' + date + '&adults=' + adults + '&childs=' + childs + '&infants=' + infants + '&sortType0=price&sortOrder0=sortAsc&page=loaded'
        client_response = Client(url)
        self.source = client_response.mainFrame().toHtml()

    def GetLength(self):
        soup = BeautifulSoup(self.source, "lxml")
        data = []
        for table in soup.findAll('th', {'class': 'price'}):
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
        for table in soup.findAll('th', {'class':'price'}):
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
        for table in soup.findAll('th', {'class':'vendor'}):
            data.append(table.text)
        return self.FixData(data,self.GetLength())
    def GetDictionary(self):
        dict = {}
        list1 = self.GetPrices()
        list2 = self.GetDepartureTime()
        list3 = self.GetDurationTime()
        list4 = self.GetStops()
        list5 = self.GetArrivalTime()
        list6 = self.GetRoute()
        list7 = self.GetVendor()
        for position in range(0,self.GetLength()):
            dict[position+1] = [list1[position],list2[position],list3[position],list4[position],list5[position],list6[position],list7[position]]
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
