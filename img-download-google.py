#!/usr/bin/env python

# Download the google image search images for the given keyword, to keyword folder
#
# Set up:
#   pip install beautifulsoup4
#
# Command line inputs: None
# In file inputs: Give the image url as IMAGE_URL
# Runtime inputs: None


from bs4 import BeautifulSoup
import requests
import re
import urllib2
import os
import cookielib
import json

MAX_IMAGES = 9
QUERY = "waterfall wallpapers"#you can change the query for the image  here
image_name = "Image"

query = QUERY.split()
query = '+'.join(query)
URL = "https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
print URL

# add the directory for your image here
header = {
	'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}

def get_soup(url, header):
    openurl = urllib2.Request(url,headers=header)
    urlopen = urllib2.urlopen(openurl)
    return BeautifulSoup(urlopen, 'html.parser')

soup = get_soup(URL,header)
#print soup

ActualImages=[]# contains the link for Large original images, type of  image
COUNT=0
for a in soup.find_all("div",{"class":"rg_meta"}):
    COUNT+=1
    if COUNT>MAX_IMAGES:
        break
    link, Type = json.loads(a.text)["ou"], json.loads(a.text)["ity"]
    ActualImages.append((link,Type))

#print "there are total", len(ActualImages),"images"
DIR = query.split()[0]
if not os.path.exists(DIR):
    os.mkdir(DIR)

## print images
for i, (img, Type) in enumerate(ActualImages):
    try:
        req = urllib2.Request(img, headers=header)#{'User-Agent' : header})
        raw_img = urllib2.urlopen(req).read()

        ext = 'jpg' if len(Type)==0 else Type
        img_name = image_name+"_"+str(i)+"."+ext

        f = open(os.path.join(DIR, img_name), 'wb')    
        f.write(raw_img)
        f.close()
    
    except Exception as e:
        print "could not load : "+img
        print e            