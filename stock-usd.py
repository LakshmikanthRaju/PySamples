#!/usr/bin/env python

# Get USD to INR exchange rate, the latest stock price (NYSE) - input stock code
#
# Set up: pip install beautifulsoup4
#
# Command line inputs: None
# In file inputs:
#   Give Stock code in STOCK url
#   Give currency code in CURRENCY url
# Runtime inputs: None

from urllib2 import Request, urlopen, URLError

#Tag Format: symbol, value, date, time, change, open value, day's high, day's low, volume
TAG='sl1d1t1c1ohgv'

STOCK = Request('http://finance.yahoo.com/d/quotes.csv?s=VMW&f=sl1d1t1co&e=.csv')
CURRENCY = Request('http://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1c1o&s=USDINR=X')
#gold = Request('http://www.xmlcharts.com/cache/precious-metals.php') #obsolete

def get_vmw():
    try:
        response = urlopen(STOCK)
        value = response.read()
        return value
    except URLError, e:
        return "Error while fetching stock price"
        
def get_usd():
    try:
        response = urlopen(CURRENCY)
        value = response.read()
        return value
    except URLError, e:
        return "Error while fetching USD-INR rate"

if __name__ == "__main__":
    print get_vmw()
    print get_usd()