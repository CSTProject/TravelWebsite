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
origin = 'VIDP'
dest = 'VOBL'
url = 'https://uk.flightaware.com/live/findflight?origin=' + origin + '&destination=' + dest
client_response = Client(url)
source = client_response.mainFrame().toHtml()

def routes_spider(max_pages):
    page = 1

    while page <= max_pages:

        plain_text = source
        soup = BeautifulSoup(plain_text, "lxml")
        for table in soup.findAll('table', {'id':'Results'}):
            plain_text = table.text
            print(plain_text)


        page +=1

routes_spider(1)