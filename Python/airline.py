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

class Spider(Client):
    def __init__(self, origin, destination):
        url = 'https://uk.flightaware.com/live/findflight?origin=' + origin + '&destination=' + destination
        ClObj = Client(url)
        client_response = ClObj
        self.source = client_response.mainFrame().toHtml()


    def routes_spider(self):
        soup = BeautifulSoup(self.source, "lxml")
        for table in soup.findAll('table', {'id':'Results'}):
            plain_text = table.text
            print(plain_text)



ori = 'VIDP'
dest = 'VOBL'
spider = Spider(ori,dest)
spider.routes_spider()