# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:24:08 2019

@author: Dell
"""

import os
from astropy.io import fits


findobject = '\'53753\''

os.chdir('I:/BASS/')
path = os.getcwd()


def findinfo(strfile): 
    phdulist = fits.open(strfile)
    objectname = phdulist[0].header['OBJECT']
    filtername = phdulist[0].header['FILTER']
    return objectname,filtername

good = []
for root, dirs, files in os.walk(path):
   for file in files:
       strfile = os.path.join(root, file)
       try:
           objectname,filtername = findinfo(strfile)
       except:
           continue
       #print(objectname)
       yuansu = (objectname,filtername)
       good.append(yuansu)
       if (objectname == findobject):
           print(strfile)
           print(filtername)
file = open('name.txt', 'w')
myset = set(good)
for item in myset:
    #print(item,good.count(item))
    try:
        c=''.join(item)
    except:
        continue
    file.write(c+'          '+str(good.count(item))+'\n')
file.close()