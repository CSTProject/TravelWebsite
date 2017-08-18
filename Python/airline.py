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
    def __init__(self, origin, destination):
        url = 'https://www.cleartrip.com/flights/results?from=' + origin + '&to=' + destination +'&depart_date=20/08/2017&adults=1&childs=0&infants=0&class=Economy&airline=&carrier=&intl=n&sd=1503042323330&page=loaded'
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
    def GetDurationType(self):
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


'''CODE BELOW ONLY FOR DEBUGGING AND TESTING'''
ori = ['IXC','DEL']
dest = ['IXC','DEL']
spiders = Spider(ori[1],dest[0])

temp = ["  dfdf \n","as   asd"]
print(spiders.FixData(temp,len(temp)))


list1 = spiders.GetPrices()
list2 = spiders.GetDepartureTime()
list3 = spiders.GetDurationTime()
list4 = spiders.GetDurationType()
list5 = spiders.GetArrivalTime()
list6 = spiders.GetRoute()
list7 = spiders.GetVendor()
for i in range(0,spiders.GetLength()):
    print('\n' + str(i) + '.\nPrice: ' + list1[i])
    print('\n' + '\nVendor:\n' + list7[i])
    print('\n' + '\nDeparture Time:\n' + list2[i])
    print('\n' + '\nArrival Time:\n' + list5[i])
    print('\n' + '\nDuration:\n' + list3[i])
    print('\n' + '\nJourney type :\n' + list4[i])
    print('\n' + '\nRoute:\n' + list6[i])




