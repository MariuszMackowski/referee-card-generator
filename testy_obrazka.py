# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 15:59:15 2019

@author: Mario
"""

from urllib import request

obraz1 = "photonews/24630.36745600.jpg"
obraz2 = "photonews/2600.62497200.jpg"
link = "http://ligowiec.net/"

url1 = link+obraz1
url2 = link + obraz2
f = open('1.jpg', 'wb')
f.write(request.urlopen(url1).read())
f.close()
f = open('2.jpg', 'wb')
f.write(request.urlopen(url2).read())
f.close()