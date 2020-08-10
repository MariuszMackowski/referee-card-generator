# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 15:14:21 2019

@author: Mario
"""

from bs4 import BeautifulSoup
import urllib.request as urllib2
from urllib import request

def download_logo(url, name):
    ## Download and saves clubs logos
    link = "http://ligowiec.net/"
    f = open(name, 'wb')
    f.write(request.urlopen(link+url).read())
    f.close()


def download_info(url):
    ## Download clubs names, match day and hour.
    ## Returning list of everything to fill LineEdits
    names = []    
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser') 
   
    for link in soup.find_all('a'):
        href = link.get("href")
        if 'tabela' in href:
            if not link.get_text() == '':
                liga = link.get_text()
        if "klub" in href:
            if not link.get_text() ==  "":
                names.append(link.get_text())
                print(link.get_text())
        elif "co-gdzie-kiedy" in href:
            names.append(link.get_text().replace("-",".").replace(" "," r. godz. "))
            print(link.get_text().replace("-",".").replace(" "," r. godz. "))    
    
    names.append(names[0].split(" ")[-1])    
    nazwy = ["./res/1.jpg","./res/2.jpg"]
    names = names + nazwy    
    names.append(liga)
    i = 0
    for img in soup.find_all("img"):
        src = img.get("src")
        if "news" in src:        
            download_logo(src, nazwy[i])
            i=i+1
    
    for table in soup.find_all('table'):
        if 'sędzia' in table.get_text():
            ref = table.get_text()
            break
    ref=ref.split('sędzia: ')[1].split('uzupełnij')[0]
    if not ref == '':        
        print(ref)
        ref=ref.split("\t")
        names = names + ref
        
    
    
    return names
