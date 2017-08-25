import dryscrape
from bs4 import BeautifulSoup

class Spider():
    def __init__(self, origin, destination, date, adults, childs, infants):
        url = 'https://www.cleartrip.com/flights/results?from=' + origin + '&to=' + destination + '&depart_date=' + date + '&adults=' + adults + '&childs=' + childs + '&infants=' + infants + '&sortType0=price&sortOrder0=sortAsc&page=loaded'
        self.loss = 0  # Number of indices removed during fixing dictionary
        self.losspercent = 0
        try:
            dryscrape.start_xvfb()
            session = dryscrape.Session()
            session.visit(url)
            response = session.body()
            self.source = response
            print("\nGOT DATA,STARTING SCRAPING\n")
            #print(response + "\n\n")
        except:
            print("\nWARNING : CHECK INTERNET CONNECTION, CAN'T GET DATA FROM THE INTERNET\n")
            self.source = ''

    def GetLength(self):
        soup = BeautifulSoup(self.source, "lxml")
        data = []
        for table in soup.findAll('th', {'id': 'BaggageBundlingTemplate'}):
            data.append(table.text)
        return len(data) - self.loss

    # Removes extra spaces from scraped data
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
                for elem in table:
                    imgs = elem('img')
                    if imgs:
                        data.append(imgs['alt'])
                    else:
                        data.append(table.text)

        return self.FixData(data, self.GetLength())




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

        return self.FixDict(dict)

    ''' FixData()
        Removes Entries from lists of the dictionary at a particular index,
        if at least one of the key(s) have the list index value empty.
        Basically it validates the data and checks the accuracy of the scraping algorithm.
    '''

    def FixDict(self, dictionary):

        positions = []  # positions(indices) where the list values will be deleted
        for position in range(0,self.GetLength()):
            items = [
                dictionary['Prices'][position],
                dictionary['DepartTime'][position],
                dictionary['Time'][position],
                dictionary['Time'][position],
                dictionary['Stops'][position],
                dictionary['ArrivalTime'][position],
                dictionary['Route'][position],
                dictionary['Vendor'][position]]

            # Trim the string and check if it's empty
            for x in range(8):
                items[x] = items[x].replace("\n", "")
                items[x] = items[x].replace(" ", "")
                # print(items[x])
                if items[x] == '':
                    positions.append(position)

        dictionary = self.DeleteEntry(positions, dictionary)

        #  Regenerate the messed up serial numbers due to deleting of values
        #  REQUIRED FOR DATA TO CORRECTLY SHOW UP ON THE PAGE (See jinja code on result.html)
        for x in range(0,self.GetLength()):  # DELETE all entries on 'Serial' key
            del dictionary['Serial'][0]

        for pos in range(0,self.GetLength()):  # Create fresh ordered entries for 'Serial'
            dictionary['Serial'].append(str(pos))

        print('Lost ' + str(self.loss) + ' Entry(s).\n')
        t = str(100 - self.losspercent)
        print('Scraping Accuracy : ' + t[0] + t[1] + t[2] + t[3] + t[4] + '%\n')

        return dictionary




    def DeleteEntry(self,positions,dict):
        for i in range(0,len(positions)):
            del dict['Prices'][positions[i]-i]
            del dict['DepartTime'][positions[i]-i]
            del dict['Time'][positions[i]-i]
            del dict['ArrivalTime'][positions[i]-i]
            del dict['Route'][positions[i]-i]
            del dict['Vendor'][positions[i]-i]
            del dict['Serial'][positions[i]-i]
            del dict['Stops'][positions[i]-i]

        self.loss = len(positions)
        self.losspercent = (self.loss/(self.GetLength() + self.loss)) * 100
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
print(spiders.GetDictionary())
'''