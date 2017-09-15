#!/usr/bin/env python

# Download the google image search images for the given keyword, to keyword folder
#
# Set up:
#   pip install beautifulsoup4
#   pip install requests
#
# Command line inputs: None
# In file inputs:
#   Give the search string as QUERY
#   Give the number of images to download as MAX_IMAGES (maximum 100)
# Runtime inputs: None


from bs4 import BeautifulSoup
import requests
import re
import urllib2
import os
import cookielib
import json

QUERY = "waterfall wallpapers"#you can change the query for the image  here
MAX_IMAGES = 9

query = QUERY.split()
query = '+'.join(query)
URL = "https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
IMAGE_NAME = "Image"
ActualImages=[]# contains the link for Large original images, type of  image


header = {
	'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}

def get_soup(url, header):
    openurl = urllib2.Request(url,headers=header)
    urlopen = urllib2.urlopen(openurl)
    return BeautifulSoup(urlopen, 'html.parser')

def get_image_urls(soup):
    count=0
    for a in soup.find_all("div",{"class":"rg_meta"}):
        count+=1
        if count>MAX_IMAGES:
            break
        link, Type = json.loads(a.text)["ou"], json.loads(a.text)["ity"]
        ActualImages.append((link,Type))

    print "there are total", len(ActualImages),"images"

def download_images():
    dir = query.split()[0]
    if not os.path.exists(dir):
        os.mkdir(dir)

    # download and save images
    for i, (img, Type) in enumerate(ActualImages):
        try:
            ext = 'jpg' if len(Type) == 0 else Type
            img_name = IMAGE_NAME + "_" + str(i) + "." + ext

            req = urllib2.Request(img, headers=header)#{'User-Agent' : header})
            raw_img = urllib2.urlopen(req).read()
            f = open(os.path.join(dir, img_name), 'wb')
            f.write(raw_img)
            f.close()
    
        except Exception as e:
            print "could not load : "+img
            print e


if __name__ == "__main__":
    print URL
    soup = get_soup(URL, header)
    #print soup
    get_image_urls(soup)
    download_images()