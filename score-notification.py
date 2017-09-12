#!/usr/bin/env python2

# pip install beautifulsoup4
# download and install PyQt4

import sys
import requests
from bs4 import BeautifulSoup
from time import sleep

from PyQt4.QtGui import *
from PyQt4.QtCore import *

SCORE_URL = "http://static.cricinfo.com/rss/livescores.xml"

def sendmessage(title, message):
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle(title)
    w.setGeometry(400,400,600,50)
    b = QLabel(w)
    b.setText(message)
    b.move(50,20)
    w.show()
    app.exec_()
    return

while True:
    r = requests.get(SCORE_URL)
    while r.status_code is not 200:
        r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    data = soup.find_all("description")
    score = data[1].text
    print "SCORE: " + message
    sendmessage("Score", score)
    sleep(60)