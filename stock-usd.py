from urllib2 import Request, urlopen, URLError

#Tag Format: symbol, value, date, time, change, open value, day's high, day's low, volume
tag='sl1d1t1c1ohgv'

share = Request('http://finance.yahoo.com/d/quotes.csv?s=VMW&f=sl1d1t1co&e=.csv')
inr = Request('http://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1c1o&s=USDINR=X')
#gold = Request('http://www.xmlcharts.com/cache/precious-metals.php') #obsolete

def get_vmw():
    try:
        response = urlopen(share)
        value = response.read()
        return value
    except URLError, e:
        return null
        
def get_usd():
    try:
        response = urlopen(inr)
        value = response.read()
        return value
    except URLError, e:
        return null

if __name__ == "__main__":
    print get_vmw()
    print get_usd()