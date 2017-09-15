#!/usr/bin/env python

# Get the currency exchange rate for usd in inr
#
# Set up:
#   pip install beautifulsoup4
#   pip install requests
#
# Command line inputs: None
# In file inputs: None
# Runtime inputs: None


import requests
import json
import re
from bs4 import BeautifulSoup


def get_usd_inr():
    inr_link = 'http://inr.fxexchangerate.com/'
    inr_url = 'http://usd.fxexchangerate.com/rss.xml'
    inr = dict()
    
    r = requests.get(inr_url)
    if r.status_code is not 200:
        print 'Internal Error'
        return
    
    soup = BeautifulSoup(r.text, "html.parser")
    data = soup.find_all('item')
    for val in data:
        if re.sub('<[^>]*>', '', str(val.link)) == inr_link:
            inr['title'] = re.sub('<[^>]*>', '', str(val.title))
            inr['date'] = re.sub('<[^>]*>', '', str(val.pubdate))
            inr['value'] = re.sub('<[^>]*>', '', str(val.description))
            break
    return inr

if __name__ == "__main__":    
    print json.dumps(get_usd_inr(), indent=2)