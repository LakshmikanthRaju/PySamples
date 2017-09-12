#!/usr/bin/env python

# Get the current cricket matches score in prompt window in regular intervals
#
# Set up:
#   Manually, download and install PyQt4
#   pip install beautifulsoup4
#
# Command line inputs: None
# In file inputs: Change the MATCH_INDEX ato select the required match
# Runtime inputs: None

import sys
import requests
from bs4 import BeautifulSoup
from time import sleep

from PyQt4.QtGui import *
from PyQt4.QtCore import *

MATCH_INDEX = 1
SCORE_URL = "http://static.cricinfo.com/rss/livescores.xml"

def displayDialog(title, message):
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
    score = data[MATCH_INDEX].text
    print "SCORE: " + message
    displayDialog("Score", score)
    sleep(60)