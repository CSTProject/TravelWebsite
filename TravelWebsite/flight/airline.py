import dryscrape
from bs4 import BeautifulSoup
import multiprocessing
import time
import threading

class GetData():
    def __init__(self, origin, destination, date, adults, childs, infants):
        self.url = 'https://www.cleartrip.com/flights/results?from=' + origin + '&to=' + destination + '&depart_date=' + date + '&adults=' + adults + '&childs=' + childs + '&infants=' + infants + '&sortType0=price&sortOrder0=sortAsc&page=loaded'
        self.loss = 0  # Number of indices removed during fixing dictionary
        self.losspercent = 0
        self.length = 0
        self.source = ''
    def GetSource(self):
        try:
            print("Don't forget to export DISPLAY if using bash for windows")
            dryscrape.start_xvfb()
            session = dryscrape.Session()
            session.visit(self.url)
            response = session.body()
            self.source = response
            print("\nGOT DATA,STARTING SCRAPING\n")
            #print(response + "\n\n")
        except:
            print("\nWARNING : CHECK INTERNET CONNECTION, CAN'T GET DATA FROM THE INTERNET\n")
            print("\nDid you forget export DISPLAY=:0\n")

    def GetLength(self):
        if self.length != 0:
            #self.UpdateLength()
            return self.length
        else:
            self.UpdateLength()
            return self.length

    def UpdateLength(self):
        soup = BeautifulSoup(self.source, "lxml")
        data = []
        for table in soup.findAll('th', {'id': 'BaggageBundlingTemplate'}):
            data.append(table.text)
        self.length = len(data) - self.loss

    # Removes extra spaces from scraped data
    def FixData(self, fixthis):
        for i in range(0,self.GetLength()):
            fixthis[i] = fixthis[i].replace("\n","")
            fixthis[i] = " ".join(fixthis[i].split())
            fixthis[i] = fixthis[i].strip()
        return fixthis


    def GetPrices(self):
        soup = BeautifulSoup(self.source, "lxml")
        data = []
        for table in soup.findAll('th', {'id': 'BaggageBundlingTemplate'}):
            data.append(table.text )
        return self.FixData(data)

    def GetDepartureTime(self):
        soup = BeautifulSoup(self.source, "lxml")
        data = []
        for table in soup.findAll('th', {'class':'depart'}):
            data.append(table.text)
        return self.FixData(data)
    def GetArrivalTime(self):
        soup = BeautifulSoup(self.source, "lxml")
        data = []
        for table in soup.findAll('th', {'class':'arrive'}):
            data.append(table.text)
        return self.FixData(data)
    def GetDurationTime(self):
        soup = BeautifulSoup(self.source, "lxml")
        data = []
        for table in soup.findAll('th', {'class':'duration'}):
            data.append(table.text)
        return self.FixData(data)
    def GetStops(self):
        soup = BeautifulSoup(self.source, "lxml")
        data = []
        for table in soup.findAll('td', {'class':'duration'}):
            data.append(table.text)
        return self.FixData(data)
    def GetRoute(self):
        soup = BeautifulSoup(self.source, "lxml")
        data = []
        for table in soup.findAll('td', {'class':'route'}):
            data.append(table.text)
        return self.FixData(data)
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

        return self.FixData(data)




    def GetDictionary(self,q,string):
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

        q.put(self.FixDict(dict,string))

    ''' FixData()
        Removes Entries from lists of the dictionary at a particular index,
        if at least one of the key(s) have the list index value empty.
        Basically it validates the data and checks the accuracy of the scraping algorithm.
    '''

    def FixDict(self, dictionary,string):
        temp = ''
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
        #  REQUIRED FOR DATA TO CORRECTLY SHOW UP ON THE PAGE (See jinja code on result_*.html)
        for x in range(0,self.GetLength()):  # DELETE all entries on 'Serial' key
            del dictionary['Serial'][0]

        for pos in range(0,self.GetLength()):  # Create fresh ordered entries for 'Serial'
            dictionary['Serial'].append(str(pos))

        temp += 'Lost ' + str(self.loss) + ' Entry(s).\n'
        t = str(100 - self.losspercent)
        try:
            temp += 'Scraping Accuracy : ' + t[0] + t[1] + t[2] + t[3] + t[4] + '%\n'
        except:
            temp += 'GOT NO DATA TO SCRAPE ON\n'
        string.put(temp)
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
        self.UpdateLength()
        try:
            self.losspercent = (self.loss/(self.GetLength() + self.loss)) * 100
        except:
            self.losspercent = 100
        return dict

class OneWay():
    def GetDictionary(self, origin, destination, departdate, adults, childs, infants):
        first = GetData(origin, destination, departdate, adults, childs, infants)
        t = threading.Thread(target=first.GetSource, args=())
        t.start()
        t.join()
        q = multiprocessing.Queue()
        string = multiprocessing.Queue()
        p = multiprocessing.Process(target=first.GetDictionary, args=(q,string,))
        p.start()
        t = time.time()
        while q.empty():
            pass

        tnew = time.time() - t
        print('\nScraping took ' + str(tnew)[0] + str(tnew)[1] + str(tnew)[2] + str(tnew)[3] + ' seconds\n')
        print('\n' + string.get())

        p.terminate()

        return q.get()

class RoundTrip():
    def GetDictionary(self, origin, destination, departdate, returndate, adults, childs, infants):
        data = {'Serial': [], 'Prices': [], 'DepartTime': [], 'Time': [], 'Stops': [], 'ArrivalTime': [], 'Route': [],
                'Vendor': []}
        first = GetData(origin, destination, departdate, adults, childs, infants)
        second = GetData(destination, origin, returndate, adults, childs, infants)
        t1 = threading.Thread(target=first.GetSource, args=())
        t2 = threading.Thread(target=second.GetSource, args=())

        t1.start()
        t2.start()
        t1.join()
        t2.join()

        data1 = multiprocessing.Queue()
        data2 = multiprocessing.Queue()
        string1 = multiprocessing.Queue()
        string2 = multiprocessing.Queue()

        p1 = multiprocessing.Process(target=first.GetDictionary, args=(data1,string1,))
        p2 = multiprocessing.Process(target=second.GetDictionary, args=(data2,string2,))
        p1.start()
        p2.start()

        t = time.time()
        while data1.empty() and data2.empty():
            pass
        tnew = time.time() - t
        print('\nScraping took ' + str(tnew)[0] + str(tnew)[1] + str(tnew)[2] + str(tnew)[3] + ' seconds\n')
        print('\n' + string1.get() + '\n' + string2.get() + '\n')

        one = data1.get()
        two = data2.get()

        data['Serial'].append(one['Serial'])
        data['Prices'].append(one['Prices'])
        data['DepartTime'].append(one['DepartTime'])
        data['Time'].append(one['Time'])
        data['Stops'].append(one['Stops'])
        data['ArrivalTime'].append(one['ArrivalTime'])
        data['Route'].append(one['Route'])
        data['Vendor'].append(one['Vendor'])

        data['Serial'].append(two['Serial'])
        data['Prices'].append(two['Prices'])
        data['DepartTime'].append(two['DepartTime'])
        data['Time'].append(two['Time'])
        data['Stops'].append(two['Stops'])
        data['ArrivalTime'].append(two['ArrivalTime'])
        data['Route'].append(two['Route'])
        data['Vendor'].append(two['Vendor'])

        print(data)
        p1.terminate()
        p2.terminate()

        return data



'''
CODE BELOW ONLY FOR DEBUGGING AND TESTING
print("Enter Start Location")
start = input()
print("Enter Stop Location")
end = input()
print("Enter Date1 in format dd/mm/yyyy")
date1 = input()
print("Enter Date2 in format dd/mm/yyyy")
date2 = input()
print("Enter Adults")
adults = input()
print("Enter Childs")
child = input()
print("Enter Infants")
infant = input()
print("Processing...")
oneway = OneWay()
roundtrip = RoundTrip()
print('ONE WAY TRIP\n\n')
print(oneway.GetDictionary(start,end,date1,adults,child,infant))
print('ROUND TRIP\n\n')
print(roundtrip.GetDictionary(start,end,date1,date2,adults,child,infant))

'''